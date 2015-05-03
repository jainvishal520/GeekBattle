from django import forms

class register_form(forms.Form):
	#form to be displayed while registering user
	#similar to ayf registeration form (almost)
	
	state_option=(('1','Andaman and Nicobar'),('30','Andhra Pradesh'),('2','Arunachal Pradesh'),('3','Assam'),('4','Bihar'),('31','Chandigarh'),('5','Chhattisgarh'),('32','Dadra and Nagar Haveli'),('33','Daman and Diu'),('29','Delhi'),('6','Goa'),('7','Gujarat'),('8','Haryana'),('9','Himachal Pradesh'),('10','Jammu and Kashmir'),('11','Jharkhand'),('12','Karnataka'),('13','Kerala'),('34','Lakshadweep'),('14','Madhya Pradesh'),('15','Maharashtra'),('16','Manipur'),('17','Meghalaya'),('18','Mizoram'),('19','Nagaland'),('20','Orissa'),('35','Pondicherry'),('21','Punjab'),('22','Rajasthan'),('23','Sikkim'),('24','Tamil Nadu'),('25','Tripura'),('26','Uttar Pradesh'),('27','Uttarakhand'),('28','West Bengal'))
	
	
	institute_option=(('Amity University Student','Amitian'),('Other University Student','Non-Amitian'))

	gender_option=(('male','Male'),('female','Female'))
	

	institute_filter=forms.ChoiceField(label=(u'You are a'),choices=institute_option,widget=forms.RadioSelect)
	institute=forms.CharField(label=(u'Institute'))
	prog=forms.CharField(label=(u'Programme'))
	address=forms.CharField(label=(u'Address'))
	city=forms.CharField(label=(u'City'))
	state=forms.ChoiceField(label=(u'State'),choices=state_option)
	"""country=forms.CharField(label=(u'Country'))"""
	name=forms.CharField(label=(u'Name of Participant'))
	gender=forms.ChoiceField(label=(u'Gender'),choices=gender_option,widget=forms.RadioSelect)
	#look below if time
	"""dob_day=forms.ChoiceField(label=(u'Date of Birth'))
	dob_month
	dob_year"""
	phone=forms.CharField(label=(u'Phone'),required=False)
	mobile=forms.CharField(label=(u'Mobile'))
	email=forms.EmailField(label=(u'Email Id'))
	


	
