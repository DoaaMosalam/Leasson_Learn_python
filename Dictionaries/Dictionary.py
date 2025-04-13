

convert_moth = {"Jan": "January",
                "Feb": "February",
                "Mar": "March",
                "Apr": "April",
}
print (convert_moth["Jan"])
print (convert_moth.get("Mar"))
print(convert_moth.get("mar")) #outpur is None

convert_arabic_month ={
    0 : "safer",
    1 : "Rabi al-awwal",
    2 : "Rabi al-thani",
    3 : "Jumada al-awwal",
}
print (convert_arabic_month[0])
print (convert_arabic_month.get(1))