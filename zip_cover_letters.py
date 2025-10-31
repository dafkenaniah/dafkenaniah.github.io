#!/usr/bin/env python3
"""
Cover Letter Zip Creator
Creates a zip file containing all Kenneth Davis cover letter Word documents
"""

import os
import glob
import zipfile
from datetime import datetime

class CoverLetterZipper:
    def __init__(self):
        self.desktop_path = r"C:\Users\kedavis\Desktop"
        
    def create_cover_letters_zip(self):
        """Create a zip file containing all cover letter Word documents."""
        print("🚀 Cover Letter Zip Creator")
        print("=" * 40)
        
        # Find all cover letter Word documents on Desktop
        pattern = os.path.join(self.desktop_path, "Kenneth_Davis_Cover_Letter_*.docx")
        docx_files = glob.glob(pattern)
        
        if not docx_files:
            print("❌ No cover letter Word documents found on Desktop")
            print(f"   Looking for: {pattern}")
            return False
        
        print(f"✅ Found {len(docx_files)} cover letter Word documents")
        
        # Create zip filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"Kenneth_Davis_Cover_Letters_{timestamp}.zip"
        zip_path = os.path.join(self.desktop_path, zip_filename)
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                print(f"\n📦 Creating zip file: {zip_filename}")
                
                for docx_file in sorted(docx_files):
                    filename = os.path.basename(docx_file)
                    print(f"   Adding: {filename}")
                    zipf.write(docx_file, filename)
                
                # Add a readme file to the zip
                readme_content = f"""Kenneth Davis Cover Letters Collection
Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

This zip file contains {len(docx_files)} professionally formatted cover letters:

Cover Letters Included:
"""
                for docx_file in sorted(docx_files):
                    filename = os.path.basename(docx_file)
                    company = filename.replace('Kenneth_Davis_Cover_Letter_', '').replace('.docx', '').replace('_', ' ').replace(' and ', ' & ')
                    readme_content += f"• {company}\n"
                
                readme_content += f"""
Contact Information:
• Email: KennethdavisQA@gmail.com
• Phone: 225-810-2930
• LinkedIn: https://www.linkedin.com/in/kenneth-davis-977039246/
• Portfolio: https://github.com/dafkenaniah/money

Each cover letter is customized for the specific company and role, highlighting relevant experience from Kenneth's role as QA Lead for Global AI and Automation Strategy at Sony Interactive Entertainment.

Usage Instructions:
1. Extract the zip file to access individual cover letter documents
2. Open the appropriate cover letter for your target company
3. Review and customize further if needed for specific job postings
4. Save as PDF when submitting applications

Professional Summary:
Kenneth Davis brings proven expertise in QA leadership, automation strategy, AI-enhanced analysis, and global team management with documented achievements including 179.55% efficiency improvements, $11.65M+ budget management, and international studio coordination across US, UK, and Japan.
"""
                
                # Add readme to zip
                zipf.writestr("README.txt", readme_content)
                print(f"   Adding: README.txt")
            
            print(f"\n🎉 Successfully created: {zip_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error creating zip file: {str(e)}")
            return False
    
    def list_zip_contents(self, zip_path):
        """List the contents of the created zip file."""
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                file_list = zipf.namelist()
                print(f"\n📋 Zip file contents ({len(file_list)} files):")
                for filename in sorted(file_list):
                    file_info = zipf.getinfo(filename)
                    size_kb = file_info.file_size / 1024
                    print(f"   • {filename} ({size_kb:.1f} KB)")
        except Exception as e:
            print(f"❌ Error reading zip file: {str(e)}")

def main():
    zipper = CoverLetterZipper()
    success = zipper.create_cover_letters_zip()
    
    if success:
        # Find the created zip file
        pattern = os.path.join(zipper.desktop_path, "Kenneth_Davis_Cover_Letters_*.zip")
        zip_files = glob.glob(pattern)
        
        if zip_files:
            latest_zip = max(zip_files, key=os.path.getctime)
            zipper.list_zip_contents(latest_zip)
            
            print(f"\n✅ SUCCESS: Cover letters zip file created!")
            print(f"📁 Location: {latest_zip}")
            print(f"📧 Ready to attach to job applications!")
        
    else:
        print("\n❌ FAILED: Could not create zip file")
        print("Make sure cover letter Word documents exist on Desktop")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
