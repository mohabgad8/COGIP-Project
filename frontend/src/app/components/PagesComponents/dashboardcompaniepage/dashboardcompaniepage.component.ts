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


  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.fetchData('get_all_companies').subscribe((data: any[]) => {
      const companyField = this.formFields.companies.find(field => field.label === 'Company Name');
      if (companyField) {
        companyField.options = data.map(company => company.name);
      }
    });
  }

}
