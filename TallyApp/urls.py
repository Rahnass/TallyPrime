from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('groups/',views.groups,name='groups'),
    path('m_group/<int:pk>',views.m_group,name='m_group'),
    path('s_group/<int:pk>',views.s_group,name='s_group'),
    path('ledgers/',views.ledgers,name='ledgers'),
    path('grp_alter/<int:pk>',views.grp_alter,name="grp_alter"),
    path('sub_grp_alter/<int:pk>',views.sub_grp_alter,name="sub_grp_alter"),

    path('ledger_alter/<int:pk>',views.ledger_alter,name='ledger_alter'),
    path('alter_ledger/<int:pk>',views.alter_ledger,name='alter_ledger'),
    path('ledger_bank_details/<int:pk>',views.ledger_bank_details,name='ledger_bank_details'),
    path('add_bank_details/<int:pk>',views.add_bank_details,name='add_bank_details'),
    #path('show_bdetails/',views.show_bdetails,name='show_bdetails'),
    path('ledger_cheque_details/<int:pk>',views.ledger_cheque_details,name='ledger_cheque_details'),
    path('add_cheque_details/<int:id>',views.add_cheque_details,name='add_cheque_details'),
    path('cheque_printing/<int:pk>',views.cheque_printing,name='cheque_printing'),
    path('c_printt/<int:pk>',views.c_printt,name='c_printt'), 
    path('add_cheque_dimensions/<int:id>',views.add_cheque_dimensions,name='add_cheque_dimensions'), 
]