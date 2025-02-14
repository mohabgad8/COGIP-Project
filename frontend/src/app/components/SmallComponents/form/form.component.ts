import { Component, EventEmitter, Input, Output} from '@angular/core';
import {NgForOf, NgSwitch, NgSwitchCase} from '@angular/common';
import { FormsModule } from '@angular/forms';

interface FormField {
  label: string;
  placeholder?: string;
  type: string;
  options?: string[];
  inputValue?: string; 
  selectedOption?: string;
}

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
  imports: [
    NgSwitch,
    NgSwitchCase,
    NgForOf,
    FormsModule
  ],
  standalone: true
})
export class FormComponent {
  @Input() formFields: { [key: string]: FormField[] } = {};
  @Input() activeFormKey: string = '';
  @Output() formSubmitted = new EventEmitter<any>();

  submitForm() {
    const formData = this.formFields[this.activeFormKey].map(field => {
      return {
        label: field.label,
        value: field.type === 'select' ? field.selectedOption : field.inputValue
      };
    });
    this.formSubmitted.emit(formData);
  }
  
}