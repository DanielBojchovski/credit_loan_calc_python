from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_calculate_click(self, **event_args):
    try:
      credit_amount = self.text_box_credit_amount.text
      credit_amount_replacement = credit_amount
      interest_rate = self.text_box_interest_rate.text
      years = self.text_box_years.text
      sum_of_interest = 0
      for i in range(years):
        sum_of_interest_replacement = 0
        sum_of_interest_replacement += credit_amount_replacement / 100 * interest_rate
        credit_amount_replacement -= sum_of_interest_replacement
        sum_of_interest += sum_of_interest_replacement
        
      self.text_box_total_interest.text = "{:0.3f}".format(round(sum_of_interest, 3))
      self.text_box_total_to_return.text = "{:0.3f}".format(round(sum_of_interest + credit_amount, 3))
      self.text_box_monthly_return.text = "{:0.3f}".format(round((sum_of_interest + credit_amount) / (years * 12), 3))
      
    except:
      alert("Something went wrong. Please click reset and start over. Fill out the text boxes only with positive numeric values.")

  def button_reset_click(self, **event_args):
    self.text_box_credit_amount.text = ""
    self.text_box_interest_rate.text = ""
    self.text_box_years.text = ""
    self.text_box_total_interest.text = ""
    self.text_box_total_to_return.text = ""
    self.text_box_monthly_return.text = ""
    




