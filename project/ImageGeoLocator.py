from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from tkinter import Tk, filedialog
import webbrowser


def select_image():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    return file_path


def get_exif_data(image):
    exif_data = {}
    info = image._getexif()

    if info is None:
        return None

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)

        if decoded == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]

            exif_data["GPSInfo"] = gps_data
        else:
            exif_data[decoded] = value

    return exif_data


def convert_to_degrees(value):
    def to_float(v):
        try:
            return float(v)
        except:
            return float(v.num) / float(v.den)

    d = to_float(value[0])
    m = to_float(value[1])
    s = to_float(value[2])

    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(exif_data):
    gps_info = exif_data.get("GPSInfo", {})

    if not gps_info:
        return None, None

    lat = gps_info.get("GPSLatitude")
    lat_ref = gps_info.get("GPSLatitudeRef")
    lon = gps_info.get("GPSLongitude")
    lon_ref = gps_info.get("GPSLongitudeRef")

    if lat is not None and lon is not None:
        lat = convert_to_degrees(lat)
        lon = convert_to_degrees(lon)

        if lat_ref != "N":
            lat = -lat
        if lon_ref != "E":
            lon = -lon

        return lat, lon

    return None, None


def open_google_maps(lat, lon):
    url = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lon}"
    webbrowser.open(url)


# 🚀 MAIN PROGRAM
def main():
    image_path = select_image()

    if not image_path:
        print("No image selected")
        return

    print("📂 Selected:", image_path)

    image = Image.open(image_path)
    exif_data = get_exif_data(image)

    if not exif_data:
        print("No EXIF metadata found")
        return

    lat, lon = get_lat_lon(exif_data)

    if lat is not None and lon is not None:
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")

        print("Opening Google Maps...")
        open_google_maps(lat, lon)
    else:
        print(" No GPS data found in image")


if __name__ == "__main__":
    main()