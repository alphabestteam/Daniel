import csv

interface_dest_macs = {
    '70:5a:0f:44:3d:77': 'Eth2',
    '70:5a:0f:46:30:50': 'Eth0',
    '9c:7b:ef:aa:2c:6b': 'Eth4',
    '70:5a:0d:4a:cd:c7': 'Eth7',
    '9c:7b:ef:aa:2b:b7': 'Eth5',
    'ec:b1:d7:5b:a1:b4': 'Eth6',
    'ff:ff:ff:ff:ff:ff': 'Eth4',
    'dc:4a:3e:7e:90:12': 'Eth3',
    'dc:4a:3e:7e:8f:2b': 'Eth1'
}

output_rows = []  

with open('network\input_part1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        interface = row['interface']
        src_mac = row['source_mac']
        dest_mac = row['dest_mac']
        
        if dest_mac in interface_dest_macs:
            dest_interface = interface_dest_macs[dest_mac]
        else:
            dest_interface = 'Unknown'
        
        # Check if the destination MAC address is a broadcast address
        is_broadcast = dest_mac.lower() == 'ff:ff:ff:ff:ff:ff'
        if is_broadcast:
            dest_interface = 'All'

        output_row = [dest_interface, dest_mac, src_mac]
        output_rows.append(output_row)

with open('output.csv', mode='w', newline='') as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerow(['Destination Ethernet Interface', 'Source MAC', 'Received From Ethernet Interface']) 
    output_writer.writerows(output_rows)

print("Output CSV file generated.")
