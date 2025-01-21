from .models import CustomUser

def CreateDummyUsers():

    first_names = [
    "Aarav",
    "Ishita",
    "Vivaan",
    "Ananya",
    "Arjun",
    "Diya",
    "Krishna",
    "Riya",
    "Kabir",
    "Sanya",
    "Rohan",
    "Meera",
    "Aryan",
    "Pooja",
    "Kunal"
]


    for first_name in first_names:
        email = first_name + "@gmail.com"
        username = first_name
        CustomUser.objects.create(
        first_name=first_name,
        email=email,
        username=username,
        password="test@123", 
        is_doctor = True
    )
        print(f"Created user: {first_name}")