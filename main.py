import cv2
import argparse
import urllib.parse

def capture_rtsp_image(rtsp_url, output_file):
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error opening RTSP feed")
        return

    ret, frame = cap.read()
    if not ret:
        print("Error capturing frame from RTSP feed")
        return

    cv2.imwrite(output_file, frame)
    print(f"Image captured and saved as {output_file}")

    cap.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Capture PNG image from RTSP feed')
    parser.add_argument('rtsp_url', help='RTSP feed URL')
    parser.add_argument('output_file', help='Output PNG file')
    parser.add_argument('-u', '--username', help='Username for basic authentication')
    parser.add_argument('-p', '--password', help='Password for basic authentication')
    args = parser.parse_args()

    if args.username and args.password:
        # Add username and password to the RTSP URL
        parsed_url = urllib.parse.urlparse(args.rtsp_url)
        credentials = f"{args.username}:{args.password}"
        netloc_with_auth = f"{credentials}@{parsed_url.netloc}"
        modified_url = parsed_url._replace(netloc=netloc_with_auth).geturl()
        args.rtsp_url = modified_url

    capture_rtsp_image(args.rtsp_url, args.output_file)
