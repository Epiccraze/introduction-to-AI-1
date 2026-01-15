import cv2
import time
import numpy as np
import mediapipe as mp

# ================= CAMERA (MAC SAFE) =================
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

# ================= MEDIAPIPE HANDS =================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ================= FILTERS =================
FILTERS = [None, "GRAY", "NEGATIVE", "BLUR"]
current_filter = 0

last_action_time = 0
DEBOUNCE = 1.0
pinch_active = False

# ================= FUNCTIONS =================
def apply_filter(frame, f):
    if f == "GRAY":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if f == "NEGATIVE":
        return cv2.bitwise_not(frame)
    if f == "BLUR":
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame

def dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# ================= MAIN LOOP =================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    capture = False

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        lm = hand.landmark

        thumb = (int(lm[4].x * w), int(lm[4].y * h))
        index = (int(lm[8].x * w), int(lm[8].y * h))
        middle = (int(lm[12].x * w), int(lm[12].y * h))

        for p in [thumb, index, middle]:
            cv2.circle(frame, p, 8, (0, 255, 0), -1)

        threshold = 0.05 * w
        now = time.time()

        # 📸 Pinch = Capture
        if dist(thumb, index) < threshold and not pinch_active:
            pinch_active = True
            capture = True

        if dist(thumb, index) > threshold:
            pinch_active = False

        # 🎨 Thumb + Middle = Change Filter
        if dist(thumb, middle) < threshold and now - last_action_time > DEBOUNCE:
            current_filter = (current_filter + 1) % len(FILTERS)
            last_action_time = now
            print("Filter:", FILTERS[current_filter] or "None")

    # ================= APPLY FILTER =================
    filtered = apply_filter(frame, FILTERS[current_filter])

    if FILTERS[current_filter] == "GRAY":
        display = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)
    else:
        display = filtered

    # ================= SAVE =================
    if capture:
        name = f"picture_{int(time.time())}.jpg"
        cv2.imwrite(name, display)
        print("Saved:", name)

    cv2.putText(display,
                f"Filter: {FILTERS[current_filter] or 'None'}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2)

    cv2.imshow("Mac Gesture Camera", display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()