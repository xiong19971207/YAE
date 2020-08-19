from django.db import models


class WorkhouseAge(models.Model):
    snapshot_date = models.CharField(db_column='snapshot-date', max_length=255, blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    sku = models.CharField(max_length=255, blank=True, null=True)
    fnsku = models.CharField(max_length=255, blank=True, null=True)
    asin = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(db_column='product-name', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    condition = models.CharField(max_length=255, blank=True, null=True)
    avaliable_quantity_sellable_field = models.CharField(db_column='avaliable-quantity(sellable)', max_length=255,
                                                         blank=True,
                                                         null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    qty_with_removals_in_progress = models.CharField(db_column='qty-with-removals-in-progress', max_length=255,
                                                     blank=True,
                                                     null=True)  # Field renamed to remove unsuitable characters.
    inv_age_0_to_90_days = models.CharField(db_column='inv-age-0-to-90-days', max_length=255, blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters.
    inv_age_91_to_180_days = models.CharField(db_column='inv-age-91-to-180-days', max_length=255, blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters.
    inv_age_181_to_270_days = models.CharField(db_column='inv-age-181-to-270-days', max_length=255, blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters.
    inv_age_271_to_365_days = models.CharField(db_column='inv-age-271-to-365-days', max_length=255, blank=True,
                                               null=True)  # Field renamed to remove unsuitable characters.
    inv_age_365_plus_days = models.CharField(db_column='inv-age-365-plus-days', max_length=255, blank=True,
                                             null=True)  # Field renamed to remove unsuitable characters.
    currency = models.CharField(max_length=255, blank=True, null=True)
    qty_to_be_charged_ltsf_6_mo = models.CharField(db_column='qty-to-be-charged-ltsf-6-mo', max_length=255, blank=True,
                                                   null=True)  # Field renamed to remove unsuitable characters.
    projected_ltsf_6_mo = models.CharField(db_column='projected-ltsf-6-mo', max_length=255, blank=True,
                                           null=True)  # Field renamed to remove unsuitable characters.
    qty_to_be_charged_ltsf_12_mo = models.CharField(db_column='qty-to-be-charged-ltsf-12-mo', max_length=255,
                                                    blank=True,
                                                    null=True)  # Field renamed to remove unsuitable characters.
    projected_ltsf_12_mo = models.CharField(db_column='projected-ltsf-12-mo', max_length=255, blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters.
    units_shipped_last_7_days = models.CharField(db_column='units-shipped-last-7-days', max_length=255, blank=True,
                                                 null=True)  # Field renamed to remove unsuitable characters.
    units_shipped_last_30_days = models.CharField(db_column='units-shipped-last-30-days', max_length=255, blank=True,
                                                  null=True)  # Field renamed to remove unsuitable characters.
    units_shipped_last_60_days = models.CharField(db_column='units-shipped-last-60-days', max_length=255, blank=True,
                                                  null=True)  # Field renamed to remove unsuitable characters.
    units_shipped_last_90_days = models.CharField(db_column='units-shipped-last-90-days', max_length=255, blank=True,
                                                  null=True)  # Field renamed to remove unsuitable characters.
    alert = models.CharField(max_length=255, blank=True, null=True)
    your_price = models.CharField(db_column='your-price', max_length=255, blank=True,
                                  null=True)  # Field renamed to remove unsuitable characters.
    sales_price = models.CharField(max_length=255, blank=True, null=True)
    lowest_price_new = models.CharField(max_length=255, blank=True, null=True)
    lowest_price_used = models.CharField(max_length=255, blank=True, null=True)
    recommended_action = models.CharField(db_column='Recommended action', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    healthy_inventory_level = models.CharField(db_column='Healthy Inventory Level', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recommended_sales_price = models.CharField(db_column='Recommended sales price', max_length=255, blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recommended_sale_duration_days_field = models.CharField(db_column='Recommended sale duration (days)',
                                                            max_length=255, blank=True,
                                                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    recommended_removal_quantity = models.CharField(db_column='Recommended Removal Quantity', max_length=255,
                                                    blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_cost_savings_of_recommended_actions = models.CharField(
        db_column='estimated-cost-savings-of-recommended-actions', max_length=255, blank=True,
        null=True)  # Field renamed to remove unsuitable characters.
    sell_through = models.CharField(db_column='sell-through', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    item_volume = models.CharField(db_column='item-volume', max_length=255, blank=True,
                                   null=True)  # Field renamed to remove unsuitable characters.
    volume_units = models.CharField(db_column='volume-units', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    storage_type = models.CharField(db_column='storage-type', max_length=255, blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'workhouseage'
