import csv


def price_as_number(price):
    price = price.strip("$")
    price_float = float(price)
    return price_float


class CSVReader:
    """
    .
    """
    def __init__(self):
        self.pink_morsel_data = []

    def populate(self, data_folder):
        """
        Populate the database with data imported from each spreadsheet.
        """
        # open the spreadsheets
        with open(f"{data_folder}/daily_sales_data_0.csv", "r") as data_file_0:
            with open(f"{data_folder}/daily_sales_data_1.csv", "r") as data_file_1:
                with open(f"{data_folder}/daily_sales_data_2.csv", "r") as data_file_2:
                    # prepare the csv readers
                    csv_reader_0 = csv.reader(data_file_0)
                    csv_reader_1 = csv.reader(data_file_1)
                    csv_reader_2 = csv.reader(data_file_2)
                    # populate from spreadsheets
                    self.pink_morsel_data.append(["sales", "date", "region"])
                    self.populate_data(csv_reader_0)
                    self.populate_data(csv_reader_1)
                    self.populate_data(csv_reader_2)

    def populate_data(self, csv_reader):
        """

        """
        for row_index, row in enumerate(csv_reader):
            # ignore the header row
            if row_index > 0:
                # extract each required field
                product = row[0]
                price = row[1]
                quantity = row[2]
                date = row[3]
                region = row[4]
                # insert the data into array
                if product == "pink morsel":
                    sales = price_as_number(price) * int(quantity)
                    self.pink_morsel_data.append([sales, date, region])

    def write_data_to_file(self, filename):
        with open(filename, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(self.pink_morsel_data)


if __name__ == '__main__':
    reader = CSVReader()
    reader.populate("./data")
    reader.write_data_to_file("pink_morsel_sales.csv")
