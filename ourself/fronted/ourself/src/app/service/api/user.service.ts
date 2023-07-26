import { Injectable } from '@angular/core';
import { LoginI } from '../../models/login/login.interface';
// import { ResponseI } from '../../models/login/response.interface';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private urlApi:string = "http://127.0.0.1:8000/auth/";

  constructor( private http:HttpClient) { }

  login(form:LoginI){
    return this.http.post<any>(`${this.urlApi}login/`, form).pipe(
      catchError((error) => {
        if(error.status === 401){
          return throwError('Invalid credentials.');
        }else{
          return throwError('An unexpected error ocurred.');
        }
      })
    )
  }

}
