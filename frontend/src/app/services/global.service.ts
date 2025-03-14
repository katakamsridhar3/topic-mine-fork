import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class GlobalService {

  constructor(private http: HttpClient) { }

  public baseUrl: string = '';
  public customerId: string = '';
  public developerToken: string = '';
  public geminiModel: string = 'gemini-2.0-flash'

  setBaseUrl(url: string) {
    this.baseUrl = url.endsWith('/') ? url.slice(0, -1) : url;
  }

  setCustomerId(id: string) {
    this.customerId = id;
  }

  setDeveloperToken(token: string) {
    this.developerToken = token;
  }

  setGeminiModel(model: string) {
    this.geminiModel = model;
  }

  retrieveSettingsFromBackend() {
    this.http.get(this.baseUrl + '/settings').subscribe({
      next: (response: any) => {
        this.baseUrl = response['base_url'];
        this.customerId = response['google_ads_customer_id'];
        this.developerToken = response['google_ads_developer_token'];
        this.geminiModel = response['gemini_model'];
      },
      error: (error) => {
        console.log('Error retrieving settings from backend. Details: ' + error)
        throw error;
      }
    })
  }

  saveSettingsToBackend() {
    var body: any = {}
    body['base_url'] = this.baseUrl;
    body['google_ads_customer_id'] = this.customerId;
    body['google_ads_developer_token'] = this.developerToken;
    body['gemini_model'] = this.geminiModel;


    this.http.post(this.baseUrl + '/settings', body).subscribe({
      next: (response) => {
        console.log('Success saving settings to backend')
      },
      error: (error) => {
        console.log('Error saving settings to backend. Details: ' + error)
        throw error;
      }
    });
  }
}