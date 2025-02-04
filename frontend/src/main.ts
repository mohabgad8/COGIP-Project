import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import {provideRouter} from '@angular/router';
import {AppComponent} from './app/app.component';
import {HomepageComponent} from './app/components/homepage/homepage.component';
import {InvoicepageComponent} from './app/components/invoicepage/invoicepage.component';
import {ContactpageComponent} from './app/components/contactpage/contactpage.component';
import {CompaniespageComponent} from './app/components/companiespage/companiespage.component';
import {LoginpageComponent} from './app/components/loginpage/loginpage.component';
import {DashboardpageComponent} from './app/components/dashboardpage/dashboardpage.component';

bootstrapApplication(AppComponent, {
  providers: [provideHttpClient(), provideRouter([
    {path: '', component: HomepageComponent},
    {path: 'invoices', component: InvoicepageComponent},
    {path: 'contacts', component: ContactpageComponent},
    {path: 'companies', component: CompaniespageComponent},
    {path: 'login' , component:LoginpageComponent},
    {path: 'dashboard', component: DashboardpageComponent}
  ])],
}).catch((err) => console.error(err));
