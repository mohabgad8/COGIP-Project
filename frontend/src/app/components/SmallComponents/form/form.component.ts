import { Component, Input } from '@angular/core';
import {NgForOf, NgSwitch, NgSwitchCase} from '@angular/common';

interface FormField {
  label: string;
  placeholder: string;
  type: string;
  options?: string[];
}

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
  imports: [
    NgSwitch,
    NgSwitchCase,
    NgForOf
  ],
  standalone: true
})
export class FormComponent {
  @Input() formFields: { [key: string]: FormField[] } = {};
  @Input() activeFormKey: string = '';
}
