# CRM
Customer relations management software for an e-commerce business

### Issue:
I was working with an e-commerce that produced RAID units, cables, server racks, and more. For managing customer information, inventory, shipping, and work orders we use an open source ticketing system called, "open ticket". Unfortunately, it lacked in performance for specific tasks and to display important information regarding some products, such as; firmeware numbers, type, size, connection, capacity, and UPC numbers. Records of customer RMA's were kept in an excel sheet that was not sorted properly making it difficult to refer back to any repair records. At times we would temporarily use the hard drives from inventory for testing, but had no record of the hard drives being checked out or checked in. Creating labels for produtcs was done in a seperate program that needed to be done manually by choosing the template and importing .xslx to fill in data for label.

### Features:
- GUI interface
- Data stored in local database file
- Inventory management for hard drives
- RMA page
- UPC page

### Installation:
```bash
git clone https://github.com/adylon/CRM.git
cd CRM
python etickets.py
```

### Usage:
- When you run script you will be brought to the main menu with tabs displayed: Inventory, RMA, and UPC & Labels:
<img src="img/rochm.png" width="400">

##### Inventory Tab:
- Enter any information in the search query in relevence to the option box.
- You can filter for specific dates above the item option box.
- Click search.

<img src="img/invimg.png" width="400">

- Click menu to see the following:

<img src="img/invm.png" width="400">

##### Add Hard Drive to Inventory:
- Enter hard drive information and click, "Add Drive" to submit to local database.
- Click, "Main Menu" to return back to hard drive menu.

<img src="img/ahd.png" width="400">

##### Delete Hard Drive from Inventory:
- Enter hard drive serial number and then click delete, removing hard drive data from local database.

<img src="img/dhd.png" width="400">

##### Check Out Hard Drive:
- Input serial number in the entry box. Use the option box to check in or out any hard drives for testing. Click submit when finished followed by display of hard drives still in invertory.

<img src="img/cohd.png" width="400">

##### RMA:
- Enter customer RMA information followed by submit button
- Use search query in the bottom of the page according to option box, then click search.

<img src="img/rmaimg.png" width="400">

##### UPC & Labels:
- On the left side of the page, insert information regarding RAID unit built for shipment. Click submit when finished. 
- To see RAID unit inventory use the search query on the right side. Add information in the entry box that corresponds with the option box on the left side.

<img src="img/upcimg.png" width="400">

##### Create Label:
- This page is for creating labels for shipment. Choose the brand of hard drives stored in RAID unit. Using the option box on the top middle of the page, enter the part and serial number in the entry boxes and click enter when complete. Followed by display of the label contents.

<img src="img/cl.png" width="400">
