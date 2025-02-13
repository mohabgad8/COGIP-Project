import { Routes } from '@angular/router';
import {MainLayoutComponent} from './components/PagesComponents/main-layout/main-layout.component';
import {HomepageComponent} from './components/PagesComponents/homepage/homepage.component';
import {InvoicepageComponent} from './components/PagesComponents/invoicepage/invoicepage.component';
import {ContactpageComponent} from './components/PagesComponents/contactpage/contactpage.component';
import {CompaniespageComponent} from './components/PagesComponents/companiespage/companiespage.component';
import {AlternativeLayoutComponent} from './components/PagesComponents/alternative-layout/alternative-layout.component';
import {LoginpageComponent} from './components/PagesComponents/loginpage/loginpage.component';
import {RegisterpageComponent} from './components/PagesComponents/registerpage/registerpage.component';
import {DashboardpageComponent} from './components/PagesComponents/dashboardpage/dashboardpage.component';
import {CompanyDetailsComponent} from './components/PagesComponents/company-details-page/company-details.component';
import {ContactDetailsComponent} from './components/PagesComponents/contact-details-page/contact-details.component';
import {
  DashboardinvoicepageComponent
} from './components/PagesComponents/dashboardinvoicepage/dashboardinvoicepage.component';
import {
  DashboardcontactpageComponent
} from './components/PagesComponents/dashboardcontactpage/dashboardcontactpage.component';
import {
  DashboardcompaniepageComponent
} from './components/PagesComponents/dashboardcompaniepage/dashboardcompaniepage.component';

export const routes: Routes = [
   { path: '', pathMatch: 'full', redirectTo: 'home' },
      {
        path: '', component: MainLayoutComponent,
        children: [
          { path: 'home', component: HomepageComponent },
          { path: 'invoices', component: InvoicepageComponent },
          { path: 'contacts', component: ContactpageComponent },
          { path: 'companies', component: CompaniespageComponent },
          { path: 'companies/showCompany/:companyName', component: CompanyDetailsComponent },
          { path: 'contacts/showContact/:name', component: ContactDetailsComponent }

        ]
      },
      {
        path: '', component: AlternativeLayoutComponent,
        children: [
          { path: 'login', component: LoginpageComponent },
          { path: 'register', component: RegisterpageComponent },
          { path: 'dashboard', component: DashboardpageComponent,
        children: [
          { path: 'invoices', component: DashboardinvoicepageComponent },
          { path: 'contacts', component: DashboardcontactpageComponent },
          { path: 'companies', component: DashboardcompaniepageComponent }
          ]}
        ]
      },
      { path: '**', redirectTo: 'home' }
    ]

