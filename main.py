
from netmiko import ConnectHandler

def acces_netmiko():
    router = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    connexion = ConnectHandler(**router)
    print(connexion.send_command("show clock"))

    interfaces = connexion.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

    connexion.disconnect()

def dire_salut():
    print("Salut, Git!")

print("Hello, Git!")
dire_salut()
