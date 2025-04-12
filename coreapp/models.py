from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_numnber = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class RoomType(models.Model):
    room_type_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['room_type_name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['room_type_name']),
        ]
    def __str__(self):
        return self.room_type_name
    
class Room(models.Model):
    room_number = models.CharField(max_length=10,unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    description = models.TextField(blank= True, null=True)
    image = models.ImageField(upload_to='images/room')
    type = models.CharField(max_length=20, default='room')

    class Meta:
        indexes = [
            models.Index(fields=['room_type'])
        ]


    def __str__(self):
        return f'Room {self.room_number} - {self.room_type}'
    

class Lounge(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='lounge')
    image = models.ImageField(upload_to='images/lounge')

    class Meta:
        pass

    def __str__(self):
        return self.lounge_name
    
class Auditorium(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='auditorium')
    image = models.ImageField(upload_to='images/auditorium')

    def __str__(self):
        return self.auditorium_name
    
class Booking(models.Model):
    BOOKING_TYPE_CHOICES = [('Room','Room'),('Lounge','Lounge'),('Auditorium','Auditorium')]
    STATUS_CHOICES = [
        ('Pending','Pending'),('Confirmed','Confirmed'),('Completed','Completed'),('Canceled','Canceled')
    ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    lounge = models.ForeignKey(Lounge, on_delete=models.SET_NULL, null=True,blank=True)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.SET_NULL, null=True, blank=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.booking_type} Booking - {self.guest}'
    

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed','Completed'),
        ('Failed','Failed'),
        ('Refunded','Refunded')
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255, unique=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'Payment {self.id} - {self.payment_status}'