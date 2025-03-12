import { Component } from '@angular/core';
import { FormControl, FormGroupDirective, NgForm, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { GlobalService } from '../../services/global.service';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { Toast } from 'primeng/toast';
import { Ripple } from 'primeng/ripple';

/** Error when invalid control is dirty, touched, or submitted. */
export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-settings',
  imports: [FormsModule, ReactiveFormsModule, MatInputModule, MatFormFieldModule, MatButtonModule, Toast, Ripple],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.css',
  providers: [MessageService]
})
export class SettingsComponent {
  constructor(public globalService: GlobalService, private router: Router, private messageService: MessageService) {}


  matcher = new MyErrorStateMatcher();

  isSaveButtonDisabled: boolean = true;
  isSendingRequest: boolean = false;
  requestFailed: boolean = false;

  baseUrlFormControl = new FormControl('', [Validators.required, Validators.nullValidator]);
  customerIdFormControl = new FormControl('', []);
  developerTokenFormControl = new FormControl('', []);
  geminiModelFormControl = new FormControl('', [Validators.required, Validators.nullValidator]);


  ngOnInit() {
    this.baseUrlFormControl.valueChanges.subscribe(() => this.updateSaveButtonState());
    this.geminiModelFormControl.valueChanges.subscribe(() => this.updateSaveButtonState());
  }

  updateSaveButtonState() {
    if (this.baseUrlFormControl.valid && this.geminiModelFormControl.valid) {
      this.isSaveButtonDisabled = false;
    } else {
      this.isSaveButtonDisabled = true;
    }
  }

  goBack() {
    this.router.navigateByUrl('/home');
  }

  showToast(severity: string, summary: string, detail: string) {
    this.messageService.add({ severity: severity, summary: summary, detail: detail, sticky: true });
  }

  saveSettings() {
    if (this.customerIdFormControl.value === '' || this.developerTokenFormControl.value === '') {
      this.showToast('warn', 'Warning', 'If any of the fields "Google Ads Customer ID" or "Google Ads developer token" is not present, the Google Ads Keyword Planner will NOT be used to generate keywords. Instead, if keyword generation is enabled, Gemini will be used.')
    }

    this.globalService.setBaseUrl(this.baseUrlFormControl.value!);
    this.globalService.setCustomerId(this.customerIdFormControl.value!.replaceAll('-', ''));
    this.globalService.setDeveloperToken(this.developerTokenFormControl.value!);
    this.globalService.setGeminiModel(this.geminiModelFormControl.value ?? 'gemini-2.0-flash');
  }

}
