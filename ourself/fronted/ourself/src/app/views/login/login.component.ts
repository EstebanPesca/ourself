import { Component } from '@angular/core';

import { FormGroup, FormControl, Validators } from '@angular/forms';
import { UserService } from '../../service/api/user.service';
import { LoginI } from '../../models/login/login.interface';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  loginForm; FormGroup:any;

  constructor(private userService:UserService){
    this.loginForm = new FormGroup({
      username: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
    })
  }

  onLogin(){
    const formData:LoginI = {
      username: this.loginForm.get('username')?.value || '',
      password: this.loginForm.get('password')?.value || '',
    };
    this.userService.loginByEmail(formData).subscribe(data => {
      console.log(data);
    });
  }

}
