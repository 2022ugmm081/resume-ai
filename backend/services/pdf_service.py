from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def create_resume_pdf(student_name: str, resume_content: str) -> bytes:
    """
    Create a PDF resume from formatted text content
    Returns PDF as bytes
    """
    try:
        # Create PDF in memory
        pdf_buffer = BytesIO()
        
        # Create document
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
        )
        
        # Container for PDF elements
        elements = []
        
        # Get styles
        styles = getSampleStyleSheet()
        
        # Create custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=6,
            alignment=1,  # Center alignment
            fontName='Helvetica-Bold'
        )
        
        section_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=11,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=6,
            spaceBefore=8,
            fontName='Helvetica-Bold',
            borderBottom=1,
            borderColor=colors.HexColor('#34495e'),
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=10,
            leading=12,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=4,
        )
        
        # Parse and add content to PDF
        lines = resume_content.split('\n')
        
        for line in lines:
            stripped = line.strip()
            
            # Skip empty lines
            if not stripped:
                elements.append(Spacer(1, 0.05*inch))
                continue
            
            # Check if it's a section header (all caps with = signs)
            if stripped.startswith('=') and '=' in stripped[1:]:
                continue
            
            # Check if line contains section headers
            if stripped in ['PROFESSIONAL SUMMARY', 'PROFESSIONAL EXPERIENCE', 'SKILLS', 
                          'EDUCATION', 'ADDITIONAL INFORMATION', 'PROJECTS', 'CERTIFICATIONS']:
                elements.append(Paragraph(stripped, section_style))
                elements.append(Spacer(1, 0.05*inch))
            
            # Name at top (first non-empty line typically)
            elif len(stripped) > 20 and all(c.isupper() or c.isspace() for c in stripped) and 'Email' not in stripped:
                if not any(isinstance(el, Paragraph) and student_name.upper() in str(el) for el in elements):
                    elements.append(Paragraph(stripped, title_style))
                    elements.append(Spacer(1, 0.08*inch))
            
            # Contact info
            elif 'Email:' in stripped or 'Phone:' in stripped or 'Location:' in stripped:
                elements.append(Paragraph(stripped, body_style))
            
            # Regular text
            else:
                # Check if it's a bullet point
                if stripped.startswith('•') or stripped.startswith('-'):
                    bullet_style = ParagraphStyle(
                        'Bullet',
                        parent=body_style,
                        leftIndent=20,
                        bulletIndent=10,
                    )
                    elements.append(Paragraph(stripped, bullet_style))
                else:
                    # Check if it's bold text (job titles, company names)
                    if any(keyword in stripped for keyword in ['Company', 'Position', 'Institution', 'Degree']):
                        bold_style = ParagraphStyle(
                            'BoldText',
                            parent=body_style,
                            fontName='Helvetica-Bold'
                        )
                        elements.append(Paragraph(stripped, bold_style))
                    else:
                        elements.append(Paragraph(stripped, body_style))
        
        # Build PDF
        doc.build(elements, canvasmaker=NumberedCanvas)
        
        # Get PDF bytes
        pdf_buffer.seek(0)
        pdf_bytes = pdf_buffer.getvalue()
        
        logger.info(f"PDF created successfully for {student_name}")
        return pdf_bytes
    
    except Exception as e:
        logger.error(f"Error creating PDF: {str(e)}")
        raise


class NumberedCanvas(canvas.Canvas):
    """Canvas class to add page numbers"""
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_state = None

    def showPage(self):
        self._saved_state = self.getState()
        self._saved_state.matrix = self._saved_state.matrix[:]
        self._saved_state.font = self._saved_state.font
        canvas.Canvas.showPage(self)

    def save(self):
        num_pages = self._pageNumber
        if self._saved_state is None:
            canvas.Canvas.save(self)
            return

        # Seek to beginning
        for page_num in range(1, num_pages + 1):
            self._pageNumber = page_num
            self.drawString(
                7.6 * 72,
                0.3 * 72,
                f"Page {page_num}"
            )
        canvas.Canvas.save(self)


def save_resume_to_file(pdf_bytes: bytes, filename: str) -> str:
    """
    Save PDF bytes to a file
    Returns the file path
    """
    try:
        filepath = f"resumes/{filename}.pdf"
        
        # Create directory if it doesn't exist
        import os
        os.makedirs("resumes", exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(pdf_bytes)
        
        logger.info(f"Resume saved to {filepath}")
        return filepath
    
    except Exception as e:
        logger.error(f"Error saving PDF file: {str(e)}")
        raise
