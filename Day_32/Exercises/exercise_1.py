import smtplib
my_email= "PyBoy007@outlook.com"
password ="Py@112233"
connection=smtplib.SMTP("smtp.outlook.com",port=587)
connection.starttls() # tls stand for (trasnport layer security.)
with smtplib.SMTP(user=my_email, password=password) as connection:
    connection.sendmail(
        from_addr=my_email,
        to_addrs="syednimra92@gmail.com",msg="Subject:Hello I'm here\n\nthis is the content"
        )
    
    print("Done!!")
    connection.quit()