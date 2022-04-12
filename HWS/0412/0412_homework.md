# 0412_homework

1. User Model BooleanField

```python
 is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
```



```python
 is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
```



2. username max length

150자



3. login validation

`is_Authenticated`



4. Login 기능 구현

(a) : AuthenticationForm

(b) : login

(c) : form.get_user()



5. who are you?

AnonymousUser



6. 암호화 알고리즘

input이 같을 때 output이 같은 함수를 해시 함수라고 한다.

 Django uses the [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithm with a SHA256 hash, a password stretching mechanism recommended by [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf). This should be sufficient for most users: it’s quite secure, requiring massive amounts of computing time to break.

[PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithm을 사용하고, SHA256 해시 함수를 사용한다.



7. Logout 기능 구현

logout을 import 할 때 as auth_logout 이라는 이름으로 붙여서 가져온다.