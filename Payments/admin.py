from django.contrib import admin

from .models import Payment, Refund, Payout, Transaction


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('fee_amount', 'order', 'amount', 'currency', 'status', 'payment_method', 'created_at' ,'updated_at' ,'net_amount' , 'paid_at' )
    search_fields = ('order__order_number',  'payment_id')
    list_filter = ('status', 'payment_method', 'created_at' 'updated_at')
    readonly_fields = ('created_at', 'updated_at' 'paid_at')


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ( 'order' , ' Payment',  'refund_id' , 'currency' ,'amount', 'staus', 'created_at', 'updated_at')
    search_fields = ('order__order_number',  'refund_id')
    list_filter = ('staus', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ('order', 'payout_id',  'amount', 'currency', 'status', 'created_at', 'updated_at')
    search_fields = ('order__order_number', 'payout_seller__business_name' )
    list_filter = ('status', 'created_at', 'updated_at')
    readonly_fields = ('created_at')