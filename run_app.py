from utils.operations.menu import CustomsCalculator

dutiable_value = 0
dutiable_frt = 0
dutiable_ins = 0
rate_of_exchange = 0
customs_duty = 0
total_dutiable_value = 0
rate_of_duty = 0
bank_charge = 0
brokerage_fee = 0
arrastre_charge = 0
wharfage_due = 0
import_processing_fee = 0
customs_documentary_stamp = 0
type_of_entry = 0
type_of_ton = 0
total_mt_or_rt = 0
total_mt = 0
size_of_container = 0
number_of_containers = 0
type_of_shutout_export_container = 0
classification_of_dangerous_cargo = 0
landed_cost_vat = 0
value_added_tax_sop = 0
excise_tax = 0
container_security_fee_sop = 0
advance_deposit = 0
individual_fob = 0
total_fob = 0


if __name__ == '__main__':
    app = CustomsCalculator(
        dutiable_value,
        dutiable_frt,
        dutiable_ins,
        rate_of_exchange,
        customs_duty,
        total_dutiable_value,
        rate_of_duty,
        bank_charge,
        brokerage_fee,
        arrastre_charge,
        wharfage_due,
        import_processing_fee,
        customs_documentary_stamp,
        type_of_entry,
        type_of_ton,
        total_mt_or_rt,
        total_mt,
        size_of_container,
        number_of_containers,
        type_of_shutout_export_container,
        classification_of_dangerous_cargo,
        landed_cost_vat,
        value_added_tax_sop,
        excise_tax,
        container_security_fee_sop,
        advance_deposit,
        individual_fob,
        total_fob
    )
    app.get_user_input()
