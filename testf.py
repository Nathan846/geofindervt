from geofinder_vt import ImageExtractor

input_csv = "example.csv"  # Path to your CSV file containing geolocation data
directory_prefix = "GH"  # Directory prefix to filter relevant folders
extractor = ImageExtractor.ImageExtractor(input_csv, directory_prefix)
destination_path = extractor.run()
print(f"Processed files moved to: {destination_path}")