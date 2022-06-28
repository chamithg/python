from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.item import Item
from flask import flash
import re


class Dept:
    def __init__(self):
        
        self.total_prev_sales = 0
        self.total_prev_sales_target = 0
        self.total_prev_cost =0
        self.total_prev_income = 0
        self.total_prev_shrink = 0
        self.total_prev_shrink_target = 0
        self.total_nxt_sales_proj =0
        self.total_nxt_sales_target =0
        self.total_nxt_cost_proj =0
        self.total_nxt_income_proj =0
        self.total_nxt_shrink_proj =0
        self.total_nxt_shrink_target =0
        
    @classmethod
    def get_totals(cls,data):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id WHERE dept_id = %(dept_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        items =[]
        total_prev_sales = 0
        total_prev_sales_target = 0
        total_prev_cost =0
        total_prev_shrink = 0
        total_prev_shrink_target = 0
        total_nxt_sales_proj =0
        total_nxt_sales_target =0
        total_nxt_cost_proj =0
        total_nxt_shrink_proj =0
        total_nxt_shrink_target =0
    
        if results:
            for item in results:
                items.append(Item(item))
        for item in items:
            total_prev_sales += (item.prev_week_sale * item.unit_price_old)
            total_prev_sales_target += (item.prev_week_target * item.unit_price_old)
            total_prev_cost += (item.prev_week_sale * item.cost_old)
            total_prev_shrink += (item.prev_week_shrink * item.unit_price_old)
            total_prev_shrink_target +=(item.prev_week_shrink_target * item.unit_price_old)
            total_nxt_sales_proj += (item.nxt_week_sale_proj * item.unit_price_new)
            total_nxt_sales_target += (item.nxt_week_target * item.unit_price_new)
            total_nxt_cost_proj += (item.nxt_week_sale_proj * item.cost_old)
            total_nxt_shrink_proj += (item.nxt_week_shrink_proj * item.unit_price_new)
            total_nxt_shrink_target += (item.nxt_week_shrink_target * item.unit_price_new)
        
        cls.total_prev_sales = round(total_prev_sales,2)
        cls.total_prev_cost =round(total_prev_cost,2)
        cls.total_prev_income = round((total_prev_sales - total_prev_cost),2)
        cls.total_prev_shrink = round(total_prev_shrink,2)
        cls.total_nxt_sales_proj =round(total_nxt_sales_proj,2)
        cls.total_nxt_cost_proj =round(total_nxt_cost_proj,2)
        cls.total_nxt_income_proj =round((total_nxt_sales_proj - total_nxt_cost_proj),2)
        cls.total_nxt_shrink_proj =round(total_nxt_shrink_proj,2)
        cls.total_prev_sales_target = round(total_prev_sales_target,2)
        cls.total_prev_shrink_target = round(total_prev_shrink_target,2)
        cls.total_nxt_sales_target =round(total_nxt_sales_target,2)
        cls.total_nxt_shrink_target =round(total_nxt_shrink_target)
        

        return items