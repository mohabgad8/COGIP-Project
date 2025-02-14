import { Component, OnInit } from '@angular/core';

import { FormComponent } from '../../SmallComponents/form/form.component';
import {ApiService} from '../../../service/api.service';


interface FormField {
  label: string;
  placeholder?: string;
  type: string;
  options?: string[];
  inputValue?: string;
  selectedOption?: string; 
}

@Component({
  selector: 'app-dashboardcontactpage',
  standalone: true,
  imports: [FormComponent],
  templateUrl: './dashboardcontactpage.component.html',
  styleUrls: ['./dashboardcontactpage.component.css']
})
export class DashboardcontactpageComponent implements OnInit {
  formFields: { contacts: FormField[] } = {
    contacts: [
      { label: 'Contact Name', placeholder: 'Ex: John Doe', type: 'text', inputValue: '' },
      { label: 'Company', placeholder: 'Select a company', type: 'select', options: [], selectedOption: '' },
      { label: 'Email', placeholder: 'Ex: contact@exemple.com', type: 'email', inputValue: '' },
      { label: 'Phone', placeholder: 'Ex: +32 456 789 012', type: 'tel', inputValue: '' }
    ]
  };
  
  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.fetchData('get_all_companies').subscribe((data: any[]) => {
  
      const companyField = this.formFields.contacts.find(field => field.label === 'Company');
      if (companyField) {
        companyField.options = data.map(company => company.name);
      }
    });
  
  }
  submitContact(formData: any) {
  
    const formattedData = {
      name: formData.find((field: any) => field.label === "Contact Name")?.value || "",
      email: formData.find((field: any) => field.label === "Email")?.value || "",
      phone: formData.find((field: any) => field.label === "Phone")?.value || "",
      company_name: formData.find((field: any) => field.label === "Company")?.value || "",
    };
  
    this.apiService.postData(formattedData, 'add_contact').subscribe(
      response => console.log('Contact added successfully!', response),
      error => console.error('Error adding contact:', error)
    );
  }
  
  
  
}
