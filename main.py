from PIL import Image
import pytesseract

def process_image(image_name, lang_code):
	return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_eng = process_image("1_test_eng.png", "eng")
	data_fra = process_image("2_test_fra.png", "fra")
	print("******************eng**********************")
	print_data(data_eng)
	print("******************fra**********************")
	print_data(data_fra)
	output_file("1_eng.txt", data_eng)
	output_file("2_fra.txt", data_fra)

# programme pricipal
if  __name__ == '__main__':
	main()