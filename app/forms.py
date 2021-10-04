from django import forms

class FeatureNameForm(forms.Form):
    id = forms.CharField(max_length=100, label='id')
    type = forms.CharField(max_length=100, label='種類')
    region = forms.CharField(max_length=100, label='地域')
    prefecture = forms.CharField(max_length=100, label='都道府県名',required=False)
    city = forms.CharField(max_length=100, label='市区町村名',required=False)
    district = forms.CharField(max_length=100, label='地区名',required=False)
    station_name = forms.CharField(max_length=100, label='最寄駅：名称',required=False)
    station_distance = forms.CharField(max_length=100, label='最寄駅：距離（分）',required=False)
    floor_plan = forms.CharField(max_length=100, label='間取り',required=False)
    area = forms.ChoiceField(label='面積（㎡）', choices=[(x, x) for x in range(40, 510, 20)],required=False)
    shape = forms.CharField(max_length=100, label='土地の形状',required=False)
    frontage = forms.CharField(max_length=100, label='間口',required=False)
    age = forms.CharField(max_length=100, label='建築年',required=False)
    structure = forms.CharField(max_length=100, label='建物の構造',required=False)
    use = forms.CharField(max_length=100, label='用途',required=False)
    use_after = forms.CharField(max_length=100, label='今後の利用目的',required=False)
    front_direction = forms.CharField(max_length=100, label='前面道路：方位')
    front_type = forms.CharField(max_length=100, label='前面道路：種類')
    front_width = forms.CharField(max_length=100, label='前面道路：幅員（ｍ）')
    city_planning = forms.CharField(max_length=100, label='都市計画',required=False)
    floor_area_ratio = forms.ChoiceField(label='建ぺい率（％）', choices=[(x, x) for x in range(30, 90, 10)],required=False)
    volume = forms.ChoiceField(label='容積率（％）', choices=[(x, x) for x in range(200, 450, 50)],required=False)
    transaction = forms.CharField(max_length=100, label='取引時点',required=False)
    reform = forms.CharField(max_length=100, label='改装',required=False)
    caution = forms.CharField(max_length=100, label='取引の事情等',required=False)