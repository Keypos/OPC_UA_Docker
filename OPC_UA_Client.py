from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"

client = Client(url)

client.connect()

print("Client Connected")

try:
    while True:
        Dat = client.get_node("ns=2;i=4")
        Temp = client.get_node("ns=2;i=2")
        Pres = client.get_node("ns=2;i=3")

        Pressure = Pres.get_value()
        Temperature = Temp.get_value()
        Date = Dat.get_value()

        print("Date: " + str(Date))
        print("Temperature: " + str(Temperature))
        print("Pressure: " + str(Pressure))

        time.sleep(0.8)
except KeyboardInterrupt:
    pass
print("Client closed")
client.disconnect()
