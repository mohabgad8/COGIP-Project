import { Component, OnInit } from '@angular/core';

import { FormComponent } from '../../SmallComponents/form/form.component';
import {ApiService} from '../../../service/api.service';


interface FormField {
  label: string;
  placeholder: string;
  type: string;
  options?: string[];  // On précise que 'options' est un tableau de chaînes de caractères
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
      { label: 'Contact Name', placeholder: 'Ex: John Doe', type: 'text' },
      { label: 'Company', placeholder: 'Select a company', type: 'select', options: [] },
      { label: 'Email', placeholder: 'Ex: contact@exemple.com', type: 'email' },
      { label: 'Phone', placeholder: 'Ex: +32 456 789 012', type: 'tel' }
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
    this.apiService.postData(formData, 'add_contact').subscribe(response => {
      console.log('Contact added successfully!', response);
    });
}
}
