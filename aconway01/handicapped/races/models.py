# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equibasecard(models.Model):
    equibasecard_id = models.AutoField(primary_key=True)
    carddate = models.DateField(blank=True, null=True)
    track_id = models.CharField(db_column='Track_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    track_name = models.CharField(db_column='Track_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area_id = models.CharField(db_column='Area_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    equibasestate = models.CharField(db_column='EquibaseState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    track_stage = models.CharField(db_column='Track_Stage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_bullring = models.CharField(max_length=1, blank=True, null=True)
    xml_flag = models.CharField(max_length=1, blank=True, null=True)
    isfeat = models.CharField(max_length=1, blank=True, null=True)
    frank = models.CharField(max_length=255, blank=True, null=True)
    race_number = models.CharField(db_column='Race_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    equibasetext = models.TextField(db_column='EquibaseText', blank=True, null=True)  # Field name made lowercase.
    equibasedescription = models.CharField(db_column='EquibaseDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wager_text = models.TextField(db_column='Wager_Text', blank=True, null=True)  # Field name made lowercase.
    total_purse = models.DecimalField(db_column='Total_Purse', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    post_time = models.DateTimeField(db_column='Post_Time', blank=True, null=True)  # Field name made lowercase.
    race_time = models.DateTimeField(db_column='Race_Time', blank=True, null=True)  # Field name made lowercase.
    day_eve = models.CharField(db_column='Day_Eve', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_type_desc = models.CharField(max_length=255, blank=True, null=True)
    max_claim_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    distance_unit = models.CharField(max_length=255, blank=True, null=True)
    distance_id = models.CharField(max_length=255, blank=True, null=True)
    distance_in_furlong = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    course_type = models.CharField(max_length=255, blank=True, null=True)
    pub_val = models.CharField(max_length=255, blank=True, null=True)
    distance_display = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    surface_display = models.CharField(max_length=255, blank=True, null=True)
    race_breed_type = models.CharField(max_length=255, blank=True, null=True)
    race_type = models.CharField(db_column='race_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age_restriction = models.CharField(max_length=255, blank=True, null=True)
    class_rating = models.CharField(max_length=255, blank=True, null=True)
    distance_unit_desc = models.CharField(max_length=255, blank=True, null=True)
    prog_no = models.CharField(db_column='Prog_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reg_no = models.CharField(db_column='Reg_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horse_name = models.CharField(db_column='Horse_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ct = models.CharField(max_length=255, blank=True, null=True)
    win_per = models.CharField(db_column='Win_Per', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ml_odds = models.CharField(db_column='ML_Odds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scratch_indicator = models.CharField(db_column='Scratch_Indicator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    post_pos = models.CharField(max_length=255, blank=True, null=True)
    breed_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibasecard'

class Equibasecarddaily(models.Model):
    equibasecard_id = models.AutoField(primary_key=True)
    carddate = models.DateField(blank=True, null=True)
    track_id = models.CharField(db_column='Track_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    track_name = models.CharField(db_column='Track_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area_id = models.CharField(db_column='Area_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    equibasestate = models.CharField(db_column='EquibaseState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    track_stage = models.CharField(db_column='Track_Stage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_bullring = models.CharField(max_length=1, blank=True, null=True)
    xml_flag = models.CharField(max_length=1, blank=True, null=True)
    isfeat = models.CharField(max_length=1, blank=True, null=True)
    frank = models.CharField(max_length=255, blank=True, null=True)
    race_number = models.CharField(db_column='Race_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    equibasetext = models.TextField(db_column='EquibaseText', blank=True, null=True)  # Field name made lowercase.
    equibasedescription = models.CharField(db_column='EquibaseDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wager_text = models.TextField(db_column='Wager_Text', blank=True, null=True)  # Field name made lowercase.
    total_purse = models.DecimalField(db_column='Total_Purse', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    post_time = models.DateTimeField(db_column='Post_Time', blank=True, null=True)  # Field name made lowercase.
    race_time = models.DateTimeField(db_column='Race_Time', blank=True, null=True)  # Field name made lowercase.
    day_eve = models.CharField(db_column='Day_Eve', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_type_desc = models.CharField(max_length=255, blank=True, null=True)
    max_claim_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    distance_unit = models.CharField(max_length=255, blank=True, null=True)
    distance_id = models.CharField(max_length=255, blank=True, null=True)
    distance_in_furlong = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    course_type = models.CharField(max_length=255, blank=True, null=True)
    pub_val = models.CharField(max_length=255, blank=True, null=True)
    distance_display = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    surface_display = models.CharField(max_length=255, blank=True, null=True)
    race_breed_type = models.CharField(max_length=255, blank=True, null=True)
    race_type = models.CharField(db_column='race_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age_restriction = models.CharField(max_length=255, blank=True, null=True)
    class_rating = models.CharField(max_length=255, blank=True, null=True)
    distance_unit_desc = models.CharField(max_length=255, blank=True, null=True)
    prog_no = models.CharField(db_column='Prog_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reg_no = models.CharField(db_column='Reg_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horse_name = models.CharField(db_column='Horse_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ct = models.CharField(max_length=255, blank=True, null=True)
    win_per = models.CharField(db_column='Win_Per', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ml_odds = models.CharField(db_column='ML_Odds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scratch_indicator = models.CharField(db_column='Scratch_Indicator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    post_pos = models.CharField(max_length=255, blank=True, null=True)
    breed_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibasecarddaily'


class Equibasejockeys(models.Model):
    equibasejockeys_id = models.AutoField(primary_key=True)
    raceyear = models.CharField(max_length=10, blank=True, null=True)
    jockeyname = models.CharField(max_length=255, blank=True, null=True)
    winpercentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    equibaseidentity = models.CharField(max_length=255, blank=True, null=True)
    earnings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    equibaserank = models.CharField(max_length=255, blank=True, null=True)
    place = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibasestarts = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    perstart = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    topthreepercent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibaseshow = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    win = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    topthree = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibasejockeys'


class Equibaseowners(models.Model):
    equibaseowners_id = models.AutoField(primary_key=True)
    raceyear = models.CharField(max_length=10, blank=True, null=True)
    ownername = models.CharField(max_length=255, blank=True, null=True)
    winpercentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    equibaseidentity = models.CharField(max_length=255, blank=True, null=True)
    earnings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    equibaserank = models.CharField(max_length=255, blank=True, null=True)
    place = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibasestarts = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    perstart = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    topthreepercent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibaseshow = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    win = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    topthree = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibaseowners'


class Equibaserunnerinfo(models.Model):
    equibaserunnerinfo_id = models.AutoField(primary_key=True)
    trackid = models.CharField(max_length=255, blank=True, null=True)
    areaid = models.CharField(max_length=255, blank=True, null=True)
    racedate = models.DateField(blank=True, null=True)
    raceyear = models.CharField(max_length=3, blank=True, null=True)
    racemonth = models.CharField(max_length=3, blank=True, null=True)
    raceday = models.CharField(max_length=3, blank=True, null=True)
    racenumber = models.CharField(max_length=255, blank=True, null=True)
    horsename = models.CharField(max_length=255, blank=True, null=True)
    horserefno = models.CharField(max_length=255, blank=True, null=True)
    jockeyname = models.CharField(max_length=255, blank=True, null=True)
    jockeyid = models.CharField(max_length=255, blank=True, null=True)
    trainername = models.CharField(max_length=255, blank=True, null=True)
    trainerid = models.CharField(max_length=255, blank=True, null=True)
    ownername = models.CharField(max_length=255, blank=True, null=True)
    ownerid = models.CharField(max_length=255, blank=True, null=True)
    sirename = models.CharField(max_length=255, blank=True, null=True)
    damname = models.CharField(max_length=255, blank=True, null=True)
    damsirename = models.CharField(max_length=255, blank=True, null=True)
    breeder = models.CharField(max_length=255, blank=True, null=True)
    pp = models.CharField(max_length=3, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    med = models.CharField(max_length=3, blank=True, null=True)
    jockeyweight = models.CharField(max_length=4, blank=True, null=True)
    mlodds = models.CharField(max_length=255, blank=True, null=True)
    claim = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibaserunnerinfo'

class Equibaserunnerinfodaily(models.Model):
    equibaserunnerinfo_id = models.AutoField(primary_key=True)
    trackid = models.CharField(max_length=255, blank=True, null=True)
    areaid = models.CharField(max_length=255, blank=True, null=True)
    racedate = models.DateField(blank=True, null=True)
    raceyear = models.CharField(max_length=3, blank=True, null=True)
    racemonth = models.CharField(max_length=3, blank=True, null=True)
    raceday = models.CharField(max_length=3, blank=True, null=True)
    racenumber = models.CharField(max_length=255, blank=True, null=True)
    horsename = models.CharField(max_length=255, blank=True, null=True)
    horserefno = models.CharField(max_length=255, blank=True, null=True)
    jockeyname = models.CharField(max_length=255, blank=True, null=True)
    jockeyid = models.CharField(max_length=255, blank=True, null=True)
    trainername = models.CharField(max_length=255, blank=True, null=True)
    trainerid = models.CharField(max_length=255, blank=True, null=True)
    ownername = models.CharField(max_length=255, blank=True, null=True)
    ownerid = models.CharField(max_length=255, blank=True, null=True)
    sirename = models.CharField(max_length=255, blank=True, null=True)
    damname = models.CharField(max_length=255, blank=True, null=True)
    damsirename = models.CharField(max_length=255, blank=True, null=True)
    breeder = models.CharField(max_length=255, blank=True, null=True)
    pp = models.CharField(max_length=3, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    med = models.CharField(max_length=3, blank=True, null=True)
    jockeyweight = models.CharField(max_length=4, blank=True, null=True)
    mlodds = models.CharField(max_length=255, blank=True, null=True)
    claim = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibaserunnerinfodaily'


class Equibasethoroughbredhorses(models.Model):
    equibasethoroughbredhorses_id = models.AutoField(primary_key=True)
    raceyear = models.CharField(max_length=10, blank=True, null=True)
    horsename = models.CharField(max_length=255, blank=True, null=True)
    winpercentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    referencenumber = models.CharField(max_length=255, blank=True, null=True)
    earnings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    equibaserank = models.CharField(max_length=255, blank=True, null=True)
    place = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sirereference = models.CharField(max_length=255, blank=True, null=True)
    equibasestarts = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sirename = models.CharField(max_length=255, blank=True, null=True)
    speedfigure = models.CharField(max_length=255, blank=True, null=True)
    perstart = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    topthreepercent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibaseshow = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    win = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    topthree = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    registry = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibasethoroughbredhorses'


class Equibasetrainers(models.Model):
    equibasetrainers_id = models.AutoField(primary_key=True)
    raceyear = models.CharField(max_length=10, blank=True, null=True)
    trainername = models.CharField(max_length=255, blank=True, null=True)
    wpsperstarter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    earningsperstarter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    winpercentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    equibaseidentity = models.CharField(max_length=255, blank=True, null=True)
    starters = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    earnings = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    equibaserank = models.CharField(max_length=255, blank=True, null=True)
    place = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibasestarts = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    perstart = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    topthreepercent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    equibaseshow = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    win = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    startsperstarter = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    topthree = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equibasetrainers'


class RegistrationRegistrationprofile(models.Model):
    activation_key = models.CharField(max_length=64)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class RegistrationSupervisedregistrationprofile(models.Model):
    registrationprofile_ptr = models.OneToOneField(RegistrationRegistrationprofile, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'registration_supervisedregistrationprofile'
