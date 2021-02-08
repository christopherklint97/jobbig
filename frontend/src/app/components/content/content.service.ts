import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Job } from './job-card/job';

@Injectable({
  providedIn: 'root',
})
export class ContentService {
  constructor(private http: HttpClient) {}

  getJobs(source: string, title: string, city: string): Observable<Job[]> {
    return this.http.get<Job[]>('http://localhost:5000/' + source, {
      params: { title, city },
    });
  }
}
