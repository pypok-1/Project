from django.db import models


class Group(models.Model):
    office_number = models.IntegerField()
    name = models.CharField(max_length=100)
    slogan = models.TextField(blank=True)


class Student (models.Model):
    name = models.CharField(max_length=25)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    student_card_number = models.IntegerField(unique=True,max_length=20,)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class LibraryCard(models.Model):
    date_issue = models.DateField()
    expiry_date = models.DateField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='library_card')
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length= 350)
    description = models.TextField(blank=True)
    book_number = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()


class BookLoan (models.Model):
    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    librarian_name = models.CharField(max_length=500)
    loan_date = models.DateField(auto_now_add=True)
    return_date  = models.DateField(null=True,blank=True)

