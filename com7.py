import serial
import threading

def read_from_port(ser):
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
            if data:
                print(f"\nReceived on COM7 from COM5: {data}", end='', flush=True)

def write_to_port(ser):
    while True:
        user_input = input("Send to COM5: ")
        ser.write(user_input.encode('utf-8'))

def main():
    ser = serial.Serial('COM7', 9600, timeout=1)
    print(f"Connected to COM7 at 9600 baud.\nType your messages below.\n")
    read_thread = threading.Thread(target=read_from_port, args=(ser,))
    write_thread = threading.Thread(target=write_to_port, args=(ser,))

    read_thread.start()
    write_thread.start()

    read_thread.join()
    write_thread.join()

if __name__ == "__main__":
    main()