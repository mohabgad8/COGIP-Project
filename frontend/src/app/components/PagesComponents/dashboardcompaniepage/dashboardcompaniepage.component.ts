import { Component, OnInit } from '@angular/core';
import { FormComponent } from '../../SmallComponents/form/form.component';
import {ApiService} from '../../../service/api.service';


interface FormField {
  label: string;
  placeholder: string;
  type: string;
  options?: string[];
  }
@Component({
  selector: 'app-dashboardcompaniepage',
  standalone: true,
  imports: [FormComponent],
  templateUrl: './dashboardcompaniepage.component.html',
  styleUrls: ['./dashboardcompaniepage.component.css']
})

export class DashboardcompaniepageComponent implements OnInit {
  formFields: { companies: FormField[] } = {
    companies: [
      { label: 'Company Name', placeholder: 'Ex: Raviga', type: 'text' },
      { label: 'Country', placeholder: 'Select a country', type: 'select', options: [] },  
      { label: 'Type', placeholder: 'Supplier / Client', type: 'select', options: [] },
      { label: 'TVA Number', placeholder: 'BEXXXXXXXX', type: 'text' }
    ]
  };

  countries: string[] = [  "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. Swaziland)", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan",
    "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela",
    "Vietnam", "Yemen", "Zambia", "Zimbabwe"]


  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.fetchData('get_all_companies').subscribe((data: any[]) => {
      const companyField = this.formFields.companies.find(field => field.label === 'Company Name');
      if (companyField) {
        companyField.options = data.map(company => company.name);
      }
    });

    this.apiService.fetchData('get_all_types').subscribe((data: string[]) => {
      const typeField = this.formFields.companies.find(field => field.label === 'Type');
      if (typeField) {
        typeField.options = data;  
      }
    });

    const countryField = this.formFields.companies.find(field => field.label === 'Country');
    if (countryField) {
      countryField.options = this.countries;
    }
    
  }

}
