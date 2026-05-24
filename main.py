import cv2
from gesture_detector import GestureDetector
from scroll_controller import ScrollController
from config import CAMERA_INDEX, SHOW_PREVIEW

COLORS = {
    'up':   (0, 255, 100),
    'down': (0, 100, 255),
    'stop': (0, 220, 255),
    None:   (160, 160, 160)
}

LABELS = {
    'up':   '☝ Scrolling UP',
    'down': '✊ Scrolling DOWN',
    'stop': '✋ STOPPED',
    None:   'Waiting for gesture...'
}

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    detector = GestureDetector()
    scroller = ScrollController()

    print("Gesture Scroll active — press Q to quit")
    print("☝ Index finger up  → Scroll UP")
    print("✊ Fist             → Scroll DOWN")
    print("✋ Open palm        → STOP")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        gesture, hand_landmarks = detector.process(rgb)

        # Scroll only if not stopped
        if gesture in ('up', 'down'):
            scroller.scroll(gesture, delta=0.1)  # fixed delta, not movement-based

        if SHOW_PREVIEW:
            if hand_landmarks:
                detector.draw(frame, hand_landmarks)

            color = COLORS.get(gesture, COLORS[None])
            label = LABELS.get(gesture, LABELS[None])

            cv2.putText(frame, label, (10, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 2)
            cv2.putText(frame, "Q = Quit", (10, frame.shape[0] - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (180, 180, 180), 1)
            cv2.imshow("Gesture Scroll", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()