import { Component, OnInit } from '@angular/core';
import { FormComponent } from '../../SmallComponents/form/form.component';
import { ApiService } from '../../../service/api.service';

interface FormField {
  label: string;
  placeholder?: string;
  type: string;
  options?: string[];
  inputValue?: string; 
  selectedOption?: string;
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

  countries: string[] = [  
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Brazil", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Chile", "China",
    "Colombia", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
    "Kazakhstan", "Kenya", "Kuwait", "Latvia", "Lebanon", "Lithuania", "Luxembourg", "Madagascar", "Malaysia",
    "Maldives", "Mexico", "Monaco", "Mongolia", "Morocco", "Myanmar", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan", "Panama", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Saudi Arabia", "Senegal", "Serbia", "Singapore",
    "Slovakia", "Slovenia", "South Africa", "South Korea", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tanzania", "Thailand", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
  ];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    
    this.apiService.fetchData('get_all_types').subscribe((data: any[]) => {
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

  submitCompany(formData: any) {
    const formattedData = {
      name: formData.find((field: any) => field.label === "Company Name")?.value || "",
      country: formData.find((field: any) => field.label === "Country")?.value || "",
      type: formData.find((field: any) => field.label === "Type")?.value || "",
      tva: formData.find((field: any) => field.label === "TVA Number")?.value || "",
    };

    this.apiService.postData(formattedData, 'add_company').subscribe(
      response => console.log('✅ Entreprise ajoutée avec succès!', response),
      error => console.error('❌ Erreur lors de l\'ajout de l\'entreprise:', error)
    );
  }
}
