import { Component } from '@angular/core';
import {CompanyInfoComponent} from '../../SmallComponents/company-info/company-info.component';

@Component({
  selector: 'app-company-details-page',
  imports: [
    CompanyInfoComponent
  ],
  templateUrl: './company-details.component.html',
  styleUrl: './company-details.component.css'
})
export class CompanyDetailsComponent {

}
