Admin Portal Django Application
This is a simple admin portal built with Django, featuring user authentication, customer management, and invoice management.

Requirements
Python 
Django
Virtualenv 

Setup Instructions
1. Clone the Repository

git clone https://github.com/yourusername/admin_portal.git
cd admin_portal

2. Create and Activate Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Run the following commands:

python -m venv myenv
myenv\Scripts\activate

3. Install Dependencies
Install the required Python packages using pip:

pip install Django

4. Apply Migrations
Run the following command to apply database migrations:

python manage.py migrate

5. Create a Superuser
Create a superuser to access the Django admin interface:

python manage.py createsuperuser

Follow the prompts to set the username, email, and password.

6. Run the Development Server
Start the Django development server:

python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.

Usage

Accessing the Admin Portal:

-Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials to access the Django admin interface.

User Authentication:

-Signup: The signup page is the default landing page. New users can register at http://127.0.0.1:8000/signup/.
-Login: Existing users can log in at http://127.0.0.1:8000/login/.
-Logout: Users can log out at http://127.0.0.1:8000/logout/.

Customer Management:

-List Customers: Navigate to http://127.0.0.1:8000/customers/ to view a list of all customers.
-Create Customer: Navigate to http://127.0.0.1:8000/customers/create/ to add a new customer.
-Edit Customer: Navigate to http://127.0.0.1:8000/customers/edit/<customer_id>/ to edit an existing customer.

Invoice Management:
-List Invoices: Navigate to http://127.0.0.1:8000/invoices/ to view a list of all invoices.
-Create Invoice: Navigate to http://127.0.0.1:8000/invoices/create/ to create a new invoice.
-Edit Invoice: Navigate to http://127.0.0.1:8000/invoices/edit/<invoice_id>/ to edit an existing invoice.

Directory Structure:
-admin_portal/: Project directory.
	-admin_portal/: Django project settings and configurations.
	-portal/: Django app containing models, views, templates, and URL configurations.
		-migrations/: Database migrations.
		-templates/portal/: HTML templates.
		-forms.py: Forms for user signup.
		-models.py: Database models.
		-urls.py: URL routing.
		-views.py: View functions.
