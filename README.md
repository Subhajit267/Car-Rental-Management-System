# Car Rental Management System (CRMS)

A comprehensive, console-based car rental management system built with Python that supports both customer bookings and administrative management.

## 📋 Project Overview

CRMS is a feature-rich car rental management application designed for Windows systems. It provides a complete solution for car rental businesses with separate interfaces for customers and management personnel, featuring user authentication, car inventory management, booking system, and administrative controls.

## ✨ Features

### 👥 User Management
- **Dual user system**: Customers (Users) vs Management Personnel
- **Secure authentication** with password protection
- **User registration** with comprehensive profile creation
- **Account management** (update details, change passwords)
- **Profile-specific dashboards** with customized interfaces

### 🚗 Car Management
- **Complete car inventory system** with add/update/delete functionality
- **Real-time availability tracking** (Available/Booked status)
- **Car details management** (brand, model, type, ID)
- **Booking history and rental tracking**

### 📊 Booking System
- **Interactive car booking wizard**
- **Time slot and date-based reservations**
- **Real-time availability checking**
- **Booking confirmation and management**

### 🎨 Interface Features
- **Full-screen console application** with custom dimensions
- **ASCII art graphics** and visual elements
- **Progress bars** and loading animations
- **Color-coded interface** with system colors
- **gotoxy() function** for precise cursor positioning

### 🔧 Administrative Features
- **Management console** with advanced controls
- **User details viewing** for management personnel
- **Car availability updates**
- **Database management** capabilities

## 🛠️ Technical Details

### System Requirements
- **Windows OS** (XP SP3 or higher)
- **Python 3.x** installed
- **Administrative privileges** for installation

### File Structure
```
CRMS_Project/
├── setup.py              # Installation script
├── crms.py              # Main application
├── uninst.py            # Uninstall helper
├── unst.py              # Main uninstaller
└── RESOURCES/           # Additional resource files
    ├── DATABASES/
    │   ├── US_DB/       # User database
    │   └── CR_DB/       # Car database
    └── Other resources
```

### Installation
1. Run `setup.py` to install the system
2. Follow the on-screen installation wizard
3. Choose user type (User/Management) during setup
4. Create your account with required details
5. Desktop shortcut will be created automatically

### Database System
- **CSV-based data storage** for simplicity
- **User database**: Stores customer and management accounts
- **Car database**: Maintains inventory and availability
- **Rental database**: Tracks booking history

## 🚀 Usage

### Starting the Application
```bash
# After installation, run from desktop shortcut or:
python crms.py
```

### User Types & Capabilities

#### 👤 Customer (User)
- Book available cars
- View personal booking history
- Update account information
- Change password

#### 👨‍💼 Management Personnel
- All customer capabilities plus:
- Add/update/delete car details
- Manage car availability
- View all user details
- System administration

### Main Functions

#### Booking a Car
1. Login as user
2. Select "Book car" option
3. View available cars
4. Select car ID, time slot, and date
5. Confirm booking

#### Managing Inventory (Management Only)
1. Login as management
2. Access management console
3. Use car management options:
   - Add new cars
   - Update existing car details
   - Delete cars
   - Update availability status

## 🔒 Security Features

- **Password protection** with hidden input
- **User type verification**
- **Session management**
- **Data validation** for all inputs
- **Email and phone number verification**

## 🗃️ Database Schema

### User Database (usdb.csv)
- Name, User ID, Password, Email, Phone Number, Address

### Car Database (crasdb.csv)
- Car ID, Brand, Model, Type, Availability Status

### Rental Database (rtdb.csv)
- User ID, Car ID, Time Slot, Date

## 🐛 Troubleshooting

### Common Issues
1. **Installation fails**: Run as Administrator
2. **Program not starting**: Check Python installation
3. **Database errors**: Reinstall the application
4. **Display issues**: Ensure console supports full-screen mode

### Error Messages
- **Login failed**: Check credentials (5 attempts allowed)
- **Car not available**: Select different car or time slot
- **Invalid input**: Follow on-screen format requirements

## 🔄 Uninstallation

### Method 1: Using Uninstaller
1. Run `uninst.py` or use system uninstaller
2. Confirm uninstallation
3. System will remove all files and databases

### Method 2: Manual Uninstallation
```bash
# Remove installation directory
rmdir /s /q C:\CAR_RENTAL_MANAGEMENT_SYSTEM
```

## 👨‍💻 Developer Information

**Developer**: Subhajit Halder  
**Version**: 3.21 (Test Build)  
**Contact**: subhajithalder267@outlook.com  

### Technical Notes
- Built using Python standard libraries
- Uses Windows API via ctypes for console manipulation
- CSV-based data storage for simplicity
- Full-screen console application

## 📝 Version History

### v3.21 (Current)
- Enhanced user interface
- Improved database management
- Bug fixes and stability improvements

### v2.02 (Previous)
- Basic functionality implementation
- Initial release features

## 🔮 Future Enhancements

- SQL database integration
- Web interface version
- Mobile application companion
- Payment gateway integration
- Advanced reporting system
- Multi-branch support

## 📄 License

This project is provided as-is for educational and demonstration purposes. Commercial use may require additional permissions from the developer.

---

*Note: This application is designed specifically for Windows systems and requires Python 3.x to be installed on the target machine.*
