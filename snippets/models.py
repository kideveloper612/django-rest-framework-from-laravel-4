from django.db import models


class AccessLog(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot', blank=True, null=True)
    news = models.ForeignKey('News', models.DO_NOTHING, db_column='news', blank=True, null=True)
    feed = models.ForeignKey('Feed', models.DO_NOTHING, db_column='feed', blank=True, null=True)
    advertising = models.ForeignKey('Advertising', models.DO_NOTHING, db_column='advertising', blank=True, null=True)
    date = models.DateTimeField()
    module = models.CharField(max_length=45, blank=True, null=True)
    controller = models.CharField(max_length=45, blank=True, null=True)
    action = models.CharField(max_length=45, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=245, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'access_log'


class AccessLogArchive(models.Model):
    user = models.PositiveIntegerField(blank=True, null=True)
    spot = models.PositiveIntegerField(blank=True, null=True)
    news = models.PositiveIntegerField(blank=True, null=True)
    feed = models.PositiveIntegerField(blank=True, null=True)
    advertising = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    module = models.CharField(max_length=45, blank=True, null=True)
    controller = models.CharField(max_length=45, blank=True, null=True)
    action = models.CharField(max_length=45, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=245, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'access_log_archive'


class Address(models.Model):
    address_district = models.ForeignKey('AddressDistrict', models.DO_NOTHING, db_column='address_district')
    name = models.CharField(max_length=145)
    street = models.CharField(max_length=145, blank=True, null=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    complement = models.CharField(max_length=245, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'address'


class AddressCity(models.Model):
    address_state = models.ForeignKey('AddressState', models.DO_NOTHING, db_column='address_state')
    name = models.CharField(max_length=145)

    class Meta:
        db_table = 'address_city'

    def __str__(self):
        return self.name


class AddressCountry(models.Model):
    name = models.CharField(max_length=145)
    code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'address_country'

    def __str__(self):
        return self.name


class AddressDistrict(models.Model):
    address_city = models.ForeignKey(AddressCity, models.DO_NOTHING, db_column='address_city')
    name = models.CharField(max_length=145)

    class Meta:
        db_table = 'address_district'

    def __str__(self):
        return self.name


class AddressState(models.Model):
    address_country = models.ForeignKey(AddressCountry, models.DO_NOTHING, db_column='address_country')
    name = models.CharField(max_length=145)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'address_state'

    def __str__(self):
        return self.name


class Advertising(models.Model):
    advertising_type = models.ForeignKey('AdvertisingType', models.DO_NOTHING, db_column='advertising_type')
    advertising_page = models.ForeignKey('AdvertisingPage', models.DO_NOTHING, db_column='advertising_page', blank=True, null=True)
    advertising_zone = models.ForeignKey('AdvertisingZone', models.DO_NOTHING, db_column='advertising_zone', blank=True, null=True)
    campaign = models.ForeignKey('Campaign', models.DO_NOTHING, db_column='campaign', blank=True, null=True)
    file = models.CharField(max_length=245, blank=True, null=True)
    file_image = models.CharField(max_length=145, blank=True, null=True)
    file_video_mp4 = models.CharField(max_length=145, blank=True, null=True)
    file_video_mov = models.CharField(max_length=145, blank=True, null=True)
    file_video_webm = models.CharField(max_length=145, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=145)
    view_time = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=245, blank=True, null=True)
    link_target = models.CharField(max_length=45, blank=True, null=True)
    app_view = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'advertising'


class AdvertisingPage(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)
    controller = models.CharField(max_length=45, blank=True, null=True)
    action = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'advertising_page'


class AdvertisingSpot(models.Model):
    advertising = models.ForeignKey(Advertising, models.DO_NOTHING, db_column='advertising')
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot')

    class Meta:
        db_table = 'advertising_spot'


class AdvertisingType(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'advertising_type'


class AdvertisingZone(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'advertising_zone'


class Api(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=245)
    remember_token = models.CharField(max_length=45, blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'api'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        db_table = 'snippets_auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'snippets_auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'snippets_auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'snippets_auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'snippets_auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        db_table = 'snippets_auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campaign(models.Model):
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'campaign'


class Category(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'category'


class Condition(models.Model):
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot')
    date = models.DateTimeField()
    wave_height = models.FloatField(blank=True, null=True)
    wave_height_min = models.FloatField(blank=True, null=True)
    wave_height_max = models.FloatField(blank=True, null=True)
    wave_period = models.IntegerField(blank=True, null=True)
    wave_direction = models.IntegerField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_direction = models.IntegerField(blank=True, null=True)
    wind_gust = models.IntegerField(blank=True, null=True)
    water_temperature = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    weather = models.IntegerField(blank=True, null=True)
    precipitation = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'condition'


class Coupon(models.Model):
    promotion = models.ForeignKey('Promotion', models.DO_NOTHING, db_column='promotion')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    usage_limit = models.IntegerField()
    usage_restricted = models.IntegerField()
    default = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        db_table = 'coupon'


class CouponCode(models.Model):
    coupon = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='coupon')
    validity_date = models.DateTimeField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=45)
    status = models.IntegerField()

    class Meta:
        db_table = 'coupon_code'


class CouponUsage(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    coupon = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='coupon')
    coupon_code = models.ForeignKey(CouponCode, models.DO_NOTHING, db_column='coupon_code', blank=True, null=True)
    order_item = models.ForeignKey('OrderItem', models.DO_NOTHING, db_column='order_item', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'coupon_usage'


class Device(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    app_version = models.CharField(max_length=45, blank=True, null=True)
    os = models.CharField(max_length=45, blank=True, null=True)
    code = models.CharField(unique=True, max_length=245, blank=True, null=True)
    token = models.CharField(unique=True, max_length=245, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'device'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'snippets_django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'snippets_django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'snippets_django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'snippets_django_session'


class Email(models.Model):
    email_context = models.ForeignKey('EmailContext', models.DO_NOTHING, db_column='email_context')
    order_status = models.ForeignKey('OrderStatus', models.DO_NOTHING, db_column='order_status', blank=True, null=True)
    payment_status = models.ForeignKey('PaymentStatus', models.DO_NOTHING, db_column='payment_status', blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, db_column='payment_method', blank=True, null=True)
    name = models.CharField(max_length=145)
    subject = models.CharField(max_length=145)
    body = models.TextField()
    status = models.IntegerField()

    class Meta:
        db_table = 'email'


class EmailContext(models.Model):
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'email_context'


class EmailQueue(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    order = models.ForeignKey('Order', models.DO_NOTHING, db_column='order', blank=True, null=True)
    notification = models.ForeignKey('Notification', models.DO_NOTHING, db_column='notification', blank=True, null=True)
    created_at = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=245, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=245)
    cc = models.CharField(max_length=245, blank=True, null=True)
    bcc = models.CharField(max_length=245, blank=True, null=True)
    subject = models.CharField(max_length=245)
    body = models.TextField()
    status = models.IntegerField()
    smtp_response = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'email_queue'


class Feed(models.Model):
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot', blank=True, null=True)
    news = models.ForeignKey('News', models.DO_NOTHING, db_column='news', blank=True, null=True)
    sport = models.ForeignKey('Sport', models.DO_NOTHING, db_column='sport', blank=True, null=True)
    date = models.DateTimeField()
    message = models.CharField(max_length=245)
    embed_url = models.CharField(max_length=245, blank=True, null=True)
    highlight = models.IntegerField(blank=True, null=True)
    subscriber_only = models.IntegerField(blank=True, null=True)
    registered_only = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'feed'


class FeedMedia(models.Model):
    highlight = models.IntegerField(blank=True, null=True)
    feed = models.ForeignKey(Feed, models.DO_NOTHING, db_column='feed', blank=True, null=True)
    media = models.ForeignKey('Media', models.DO_NOTHING, db_column='media', blank=True, null=True)

    class Meta:
        db_table = 'feed_media'


class FeedMessage(models.Model):
    text = models.CharField(max_length=245)
    sort = models.IntegerField()

    class Meta:
        db_table = 'feed_message'


class FeedMessageOption(models.Model):
    feed_message = models.ForeignKey(FeedMessage, models.DO_NOTHING, db_column='feed_message')
    text = models.CharField(max_length=245)

    class Meta:
        db_table = 'feed_message_option'


class Media(models.Model):
    name = models.CharField(max_length=245)
    description = models.CharField(max_length=245, blank=True, null=True)
    credit = models.CharField(max_length=245, blank=True, null=True)
    file = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'media'


class Menu(models.Model):
    menu = models.PositiveIntegerField(blank=True, null=True)
    icon = models.CharField(max_length=245, blank=True, null=True)
    title = models.CharField(max_length=45)
    module = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=245)
    target = models.CharField(max_length=45, blank=True, null=True)
    order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        db_table = 'menu'


class News(models.Model):
    sport = models.ForeignKey('Sport', models.DO_NOTHING, db_column='sport', blank=True, null=True)
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField()
    title = models.CharField(max_length=145)
    lead = models.CharField(max_length=145, blank=True, null=True)
    content = models.TextField()
    keywords = models.CharField(max_length=245)
    highlight = models.IntegerField()
    subscriber_only = models.IntegerField(blank=True, null=True)
    registered_only = models.IntegerField(blank=True, null=True)
    page_title = models.CharField(max_length=145)
    page_description = models.CharField(max_length=245)
    page_keywords = models.CharField(max_length=145)
    status = models.IntegerField()

    class Meta:
        db_table = 'news'


class NewsMedia(models.Model):
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news')
    media = models.ForeignKey(Media, models.DO_NOTHING, db_column='media')
    highlight = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'news_media'


class Notification(models.Model):
    notification_status = models.ForeignKey('NotificationStatus', models.DO_NOTHING, db_column='notification_status')
    notification_filter = models.ForeignKey('NotificationFilter', models.DO_NOTHING, db_column='notification_filter')
    send_at = models.DateTimeField()
    name = models.CharField(max_length=145)
    push_priority = models.CharField(max_length=45, blank=True, null=True)
    push_data = models.TextField(blank=True, null=True)
    email_subject = models.CharField(max_length=145, blank=True, null=True)
    email_body = models.TextField(blank=True, null=True)
    sms_message = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'notification'


class NotificationFilter(models.Model):
    name = models.CharField(max_length=145, blank=True, null=True)
    description = models.CharField(max_length=245, blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'notification_filter'


class NotificationStatus(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)
    css_class = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'notification_status'


class Order(models.Model):
    order_status = models.ForeignKey('OrderStatus', models.DO_NOTHING, db_column='order_status')
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    created_at = models.DateTimeField()
    total = models.IntegerField()
    total_paid = models.IntegerField()
    total_pending = models.IntegerField()
    total_discounted = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    spotid = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spotid', blank=True, null=True,
                               related_name='order_spotid')

    class Meta:
        db_table = 'order'


class OrderData(models.Model):
    order = models.OneToOneField(Order, models.DO_NOTHING, db_column='order')
    user_name = models.CharField(max_length=45)
    user_email = models.CharField(max_length=145)
    user_cell_phone = models.CharField(max_length=15, blank=True, null=True)
    user_doc_cpf = models.CharField(max_length=45, blank=True, null=True)
    user_address_street = models.CharField(max_length=145, blank=True, null=True)
    user_address_number = models.CharField(max_length=45, blank=True, null=True)
    user_address_complement = models.CharField(max_length=145, blank=True, null=True)
    user_address_district = models.CharField(max_length=45, blank=True, null=True)
    user_address_city = models.CharField(max_length=45, blank=True, null=True)
    user_address_state = models.CharField(max_length=45, blank=True, null=True)
    user_address_country = models.CharField(max_length=45, blank=True, null=True)
    user_address_zip_code = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'order_data'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='order')
    plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='plan')
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    applied = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'order_item'


class OrderLog(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='order')
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    created_at = models.DateTimeField()
    description = models.CharField(max_length=245)
    ip_address = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'order_log'


class OrderPayment(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='order')
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, db_column='payment_method', blank=True, null=True)
    payment_gateway = models.ForeignKey('PaymentGateway', models.DO_NOTHING, db_column='payment_gateway', blank=True, null=True)
    payment_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, db_column='payment_acquirer', blank=True, null=True)
    payment_status = models.ForeignKey('PaymentStatus', models.DO_NOTHING, db_column='payment_status', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    captured_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    authorization_code = models.CharField(max_length=145, blank=True, null=True)
    order_key = models.CharField(max_length=145, blank=True, null=True)
    transaction_key = models.CharField(max_length=145, blank=True, null=True)
    instant_buy_key = models.CharField(max_length=145, blank=True, null=True)
    credit_card_brand = models.CharField(max_length=145, blank=True, null=True)
    credit_card_number = models.CharField(max_length=145, blank=True, null=True)
    credit_card_holder = models.CharField(max_length=145, blank=True, null=True)
    credit_card_date = models.DateField(blank=True, null=True)
    credit_card_cvv = models.IntegerField(blank=True, null=True)
    slip_our_number = models.CharField(max_length=245, blank=True, null=True)
    slip_bar_code = models.CharField(max_length=245, blank=True, null=True)
    slip_url = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'order_payment'


class OrderPaymentCallback(models.Model):
    order_payment = models.ForeignKey(OrderPayment, models.DO_NOTHING, db_column='order_payment')
    payment_gateway = models.ForeignKey('PaymentGateway', models.DO_NOTHING, db_column='payment_gateway')
    created_at = models.DateTimeField()
    request = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'order_payment_callback'


class OrderPaymentRequest(models.Model):
    order_payment = models.ForeignKey(OrderPayment, models.DO_NOTHING, db_column='order_payment')
    payment_gateway = models.ForeignKey('PaymentGateway', models.DO_NOTHING, db_column='payment_gateway')
    created_at = models.DateTimeField()
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'order_payment_request'


class OrderStatus(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=145, blank=True, null=True)
    css_class = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'order_status'


class Partner(models.Model):
    image = models.CharField(max_length=145, blank=True, null=True)
    name = models.CharField(max_length=145)
    sponsor = models.CharField(max_length=145, blank=True, null=True)
    note = models.CharField(max_length=245, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    foundation_date = models.DateField(blank=True, null=True)
    age_rating = models.IntegerField(blank=True, null=True)
    business_hours = models.CharField(max_length=245, blank=True, null=True)
    address = models.CharField(max_length=245, blank=True, null=True)
    address_number = models.CharField(max_length=15, blank=True, null=True)
    address_note = models.CharField(max_length=145, blank=True, null=True)
    address_district = models.CharField(max_length=45, blank=True, null=True)
    address_city = models.CharField(max_length=45, blank=True, null=True)
    address_state = models.CharField(max_length=5, blank=True, null=True)
    address_country = models.CharField(max_length=45, blank=True, null=True)
    address_postal_code = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=145, blank=True, null=True)
    site = models.CharField(max_length=145, blank=True, null=True)
    facebook = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'partner'


class PartnerCategory(models.Model):
    partner = models.ForeignKey(Partner, models.DO_NOTHING, db_column='partner')
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')

    class Meta:
        db_table = 'partner_category'


class PaymentAcquirer(models.Model):
    integration_code = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'payment_acquirer'


class PaymentGateway(models.Model):
    integration_code = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'payment_gateway'


class PaymentMethod(models.Model):
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, db_column='payment_type', blank=True, null=True)
    integration_code = models.CharField(max_length=145, blank=True, null=True)
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=245, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax_type = models.CharField(max_length=1, blank=True, null=True)
    slip_validity_days = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'payment_method'


class PaymentStatus(models.Model):
    order_status = models.ForeignKey(OrderStatus, models.DO_NOTHING, db_column='order_status', blank=True, null=True)
    integration_code = models.CharField(max_length=145, blank=True, null=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=145, blank=True, null=True)
    css_class = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'payment_status'


class PaymentType(models.Model):
    integration_code = models.CharField(max_length=145, blank=True, null=True)
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'payment_type'


class Permission(models.Model):
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu')
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'permission'


class Plan(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    days = models.IntegerField()
    free_days = models.IntegerField()
    recurrences = models.IntegerField()
    session_limit = models.IntegerField()
    page_title = models.CharField(max_length=145)
    page_description = models.CharField(max_length=245)
    page_keywords = models.CharField(max_length=145)
    status = models.IntegerField()
    quantidade_usos = models.IntegerField(blank=True, null=True)
    credits_reniew = models.IntegerField(blank=True, null=True)
    credits_reniew_date = models.DateTimeField(blank=True, null=True)
    eh_basico = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'plan'


class PlanPaymentType(models.Model):
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan')
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, db_column='payment_type')

    class Meta:
        db_table = 'plan_payment_type'


class PlanResource(models.Model):
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan')
    resource = models.ForeignKey('Resource', models.DO_NOTHING, db_column='resource')

    class Meta:
        db_table = 'plan_resource'


class PlanSpot(models.Model):
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan')
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot')

    class Meta:
        db_table = 'plan_spot'


class Promotion(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=145)
    description = models.CharField(max_length=245, blank=True, null=True)
    rule = models.TextField(blank=True, null=True)
    discount_type = models.CharField(max_length=45)
    discount_amount = models.FloatField()
    recurrences = models.IntegerField(blank=True, null=True)
    accumulative = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'promotion'


class PromotionPaymentType(models.Model):
    promotion = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='promotion')
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, db_column='payment_type')

    class Meta:
        db_table = 'promotion_payment_type'


class PromotionPlan(models.Model):
    promotion = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='promotion')
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan')

    class Meta:
        db_table = 'promotion_plan'


class PushQueue(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, db_column='device')
    notification = models.ForeignKey(Notification, models.DO_NOTHING, db_column='notification', blank=True, null=True)
    created_at = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=45)
    data = models.TextField()
    status = models.IntegerField()
    response = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'push_queue'


class Resource(models.Model):
    name = models.CharField(max_length=245)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'resource'


class Route(models.Model):
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='spot', blank=True, null=True)
    news = models.ForeignKey(News, models.DO_NOTHING, db_column='news', blank=True, null=True)
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan', blank=True, null=True)
    friendly_url = models.CharField(unique=True, max_length=245)
    redirect = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'route'


class Session(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    created_at = models.DateTimeField()
    session_code = models.CharField(max_length=245, blank=True, null=True)
    session_origin = models.CharField(max_length=15, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    note = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'session'


class Setting(models.Model):
    name = models.CharField(max_length=245)
    description = models.TextField(blank=True, null=True)
    param = models.CharField(unique=True, max_length=145)
    value = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'setting'


class SmsQueue(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    notification = models.ForeignKey(Notification, models.DO_NOTHING, db_column='notification', blank=True, null=True)
    created_at = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    cell_phone = models.CharField(max_length=15)
    message = models.CharField(max_length=245)
    status = models.IntegerField()
    response = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sms_queue'


class Sport(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'sport'


class Spot(models.Model):
    partner = models.ForeignKey(Partner, models.DO_NOTHING, db_column='partner', blank=True, null=True)
    tide = models.ForeignKey('Tide', models.DO_NOTHING, db_column='tide', blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address', blank=True, null=True)
    stream = models.CharField(max_length=245, blank=True, null=True)
    m3u8 = models.CharField(max_length=245, blank=True, null=True)
    player_embed_url = models.CharField(max_length=245, blank=True, null=True)
    camera_panel = models.CharField(max_length=245, blank=True, null=True)
    station = models.CharField(max_length=245, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    lng = models.CharField(max_length=45, blank=True, null=True)
    cover_image = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    note = models.CharField(max_length=245, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notice = models.TextField(blank=True, null=True)
    notice_is_visible = models.IntegerField(blank=True, null=True)
    viewing_time = models.IntegerField()
    subscriber_only = models.IntegerField(blank=True, null=True)
    registered_only = models.IntegerField(blank=True, null=True)
    highlight = models.IntegerField()
    page_title = models.CharField(max_length=145)
    page_description = models.CharField(max_length=245)
    page_keywords = models.CharField(max_length=145)
    order = models.IntegerField(blank=True, null=True)
    wave_height = models.FloatField(blank=True, null=True)
    wave_direction = models.IntegerField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_direction = models.IntegerField(blank=True, null=True)
    water_temperature = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    camerite = models.IntegerField(blank=True, null=True)
    magic_sea_weed = models.IntegerField(blank=True, null=True)
    windguru = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'spot'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='user')
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan', related_name='plan')
    plan_to_renew = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan_to_renew', blank=True, null=True,
                                      related_name='renew')
    created_at = models.DateTimeField()
    expiration_at = models.DateTimeField(blank=True, null=True)
    session_limit = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    order_item = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'subscription'


class SubscriptionLog(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    plan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan', related_name='log_plan')
    plan_to_renew = models.ForeignKey(Plan, models.DO_NOTHING, db_column='plan_to_renew', blank=True, null=True,
                                      related_name='log_renew')
    created_at = models.DateTimeField()
    expiration_at = models.DateTimeField(blank=True, null=True)
    session_limit = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    order_item = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'subscription_log'


class Tide(models.Model):
    name = models.CharField(max_length=245)
    description = models.CharField(max_length=245, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'tide'


class TideData(models.Model):
    tide = models.ForeignKey(Tide, models.DO_NOTHING, db_column='tide')
    date = models.DateTimeField()
    height = models.FloatField()
    moon = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tide_data'


class User(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    facebook_id = models.CharField(unique=True, max_length=145, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=145, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
    doc_cpf = models.CharField(max_length=15, blank=True, null=True)
    address_street = models.CharField(max_length=145, blank=True, null=True)
    address_number = models.CharField(max_length=15, blank=True, null=True)
    address_complement = models.CharField(max_length=145, blank=True, null=True)
    address_district = models.CharField(max_length=45, blank=True, null=True)
    address_city = models.CharField(max_length=45, blank=True, null=True)
    address_state = models.CharField(max_length=45, blank=True, null=True)
    address_country = models.CharField(max_length=45, blank=True, null=True)
    address_zip_code = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    send_email = models.IntegerField(blank=True, null=True)
    send_push = models.IntegerField(blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    activation_code = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    credits = models.IntegerField(blank=True, null=True)
    pbasic_reniew = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'user'


class UserGroup(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=145, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'user_group'


class UserGroupMenu(models.Model):
    user_group = models.ForeignKey(UserGroup, models.DO_NOTHING, db_column='user_group')
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu')

    class Meta:
        db_table = 'user_group_menu'


class UserGroupPermission(models.Model):
    user_group = models.ForeignKey(UserGroup, models.DO_NOTHING, db_column='user_group')
    permission = models.ForeignKey(Permission, models.DO_NOTHING, db_column='permission')

    class Meta:
        db_table = 'user_group_permission'


class UserPayment(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, db_column='user')
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, db_column='payment_type', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    instant_buy_key = models.CharField(max_length=145, blank=True, null=True)
    credit_card_brand = models.CharField(max_length=145, blank=True, null=True)
    credit_card_number = models.CharField(max_length=145, blank=True, null=True)
    credit_card_holder = models.CharField(max_length=145, blank=True, null=True)
    credit_card_date = models.DateField(blank=True, null=True)
    credit_card_cvv = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'user_payment'


class UserSport(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    sport = models.ForeignKey(Sport, models.DO_NOTHING, db_column='sport')

    class Meta:
        db_table = 'user_sport'
        unique_together = (('user', 'sport'),)


class UserSpot(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    spot = models.ForeignKey(Spot, models.DO_NOTHING, db_column='spot')
    accessed_at = models.DateTimeField(blank=True, null=True)
    is_credited = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_spot'
        unique_together = (('spot', 'user'),)


class UserSpotBasicPlan(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    spot = models.ForeignKey(Spot, models.DO_NOTHING, db_column='spot')
    accessed_at = models.DateTimeField(blank=True, null=True)
    is_credited = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_spot_basic_plan'
        unique_together = (('spot', 'user'),)


class UserUserGroup(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    user_group = models.ForeignKey(UserGroup, models.DO_NOTHING, db_column='user_group')

    class Meta:
        db_table = 'user_user_group'
