from discord_webhook import DiscordWebhook, DiscordEmbed
import tkinter as tk
import json

def savelink():
    webhook = webhookinput.get()
    if webhook == "":
        tk.Label(main, text="please input webhook", fg='red', bg='light gray').grid(row=2, columnspan=2)
    else:
        with open("webhook.json", "w") as f:
            json.dump(webhook, f)
        newwindow()

def newwindow():
    global main, send, titleent, descent, footent, colorent
    root = tk.Tk()
    main.destroy()
    titlelb = tk.Label(root, text="Input your title of embed(if none leave empty)").grid(row=0, column=0)
    titleent = tk.Entry(root)
    titleent.grid(row=0 , column=1)
    desclb = tk.Label(root, text="Input description of embed(everything will show in one line [ suggested use: anoucements])").grid(row=1, column=0)
    descent = tk.Entry(root)
    descent.grid(row=1,column=1)
    footerlb = tk.Label(root, text="Input your footer of embed(if none leave empty").grid(row=2, column=0)
    footent = tk.Entry(root)
    footent.grid(row=2, column=1)
    colorlb = tk.Label(root, text="Input color of your embed(must be numerical up to 7 numbers)").grid(row=3, column=0)
    colorent = tk.Entry(root)
    colorent.grid(row=3, column=1)
    send = tk.Button(root, text="Send your embed", command=send).grid(row=4, columnspan=2)
    root.mainloop()
    
def send():
    global titleent, descent, footent, colorent
    with open('webhook.json', "r") as f:
        webhookurl = json.load(f)
        print(webhookurl)
    webhook = DiscordWebhook(url=webhookurl)
    title = titleent.get()
    if title == "":
        titlec = " "
    else:
        titlec = titleent.get()
    desc = descent.get()
    if desc == "":
        descc = " "
    else:
        descc = descent.get()
    color = colorent.get()
    if color == "":
        colorc = "0000000"
    else:
        colorc = colorent.get()
    foot = footent.get()
    if foot == "":
        footc = " "
    else:
        footc = footent.get()
    embed = DiscordEmbed(title=titlec, description=descc, color=colorc)
    webhook.add_embed(embed)
    embed.set_footer(text=footc)
    webhook.execute()
def check():
    with open('webhook.json', 'r') as f:
        webhookcheck = json.load(f)
        if webhookcheck == "":
            tk.Label(main, text="There is no webhook saved", bg='Light gray', fg='red').grid(row=2, columnspan=2)
        else:
            newwindow()
main = tk.Tk()
main.config(bg="Light gray")
webhookinput = tk.Entry(main, bg="light gray")
webhookinput.grid(row=0, column=1)
webhooklabel = tk.Label(main , text='input your webhook here', bg="light gray").grid(row=0, column=0)
webhooksubmit = tk.Button(main, text="Submit", command=savelink, bg='light gray').grid(row=1, columnspan=1)
webhookload = tk.Button(main, text="load saved webhook", command=check, bg="light gray").grid(row=1, column=1)
main.mainloop()