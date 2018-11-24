import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.net.URI;
import java.util.Date;
import java.util.Locale;

import javax.print.Doc;
import javax.print.DocFlavor;
import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import javax.print.SimpleDoc;
import javax.print.attribute.Attribute;
import javax.print.attribute.DocAttributeSet;
import javax.print.attribute.HashDocAttributeSet;
import javax.print.attribute.HashPrintJobAttributeSet;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintJobAttribute;
import javax.print.attribute.PrintJobAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.PrintServiceAttribute;
import javax.print.attribute.PrintServiceAttributeSet;
import javax.print.attribute.standard.Chromaticity;
import javax.print.attribute.standard.Copies;
import javax.print.attribute.standard.DateTimeAtCompleted;
import javax.print.attribute.standard.DateTimeAtCreation;
import javax.print.attribute.standard.DateTimeAtProcessing;
import javax.print.attribute.standard.Destination;
import javax.print.attribute.standard.Fidelity;
import javax.print.attribute.standard.Finishings;
import javax.print.attribute.standard.JobHoldUntil;
import javax.print.attribute.standard.JobImpressions;
import javax.print.attribute.standard.JobImpressionsCompleted;
import javax.print.attribute.standard.JobKOctets;
import javax.print.attribute.standard.JobKOctetsProcessed;
import javax.print.attribute.standard.JobMediaSheets;
import javax.print.attribute.standard.JobMediaSheetsCompleted;
import javax.print.attribute.standard.JobMessageFromOperator;
import javax.print.attribute.standard.JobName;
import javax.print.attribute.standard.JobOriginatingUserName;
import javax.print.attribute.standard.JobPriority;
import javax.print.attribute.standard.JobSheets;
import javax.print.attribute.standard.JobState;
import javax.print.attribute.standard.JobStateReasons;
import javax.print.attribute.standard.Media;
import javax.print.attribute.standard.MediaPrintableArea;
import javax.print.attribute.standard.MediaSizeName;
import javax.print.attribute.standard.MultipleDocumentHandling;
import javax.print.attribute.standard.NumberOfDocuments;
import javax.print.attribute.standard.NumberOfInterveningJobs;
import javax.print.attribute.standard.NumberUp;
import javax.print.attribute.standard.OrientationRequested;
import javax.print.attribute.standard.OutputDeviceAssigned;
import javax.print.attribute.standard.PageRanges;
import javax.print.attribute.standard.PresentationDirection;
import javax.print.attribute.standard.PrintQuality;
import javax.print.attribute.standard.PrinterResolution;
import javax.print.attribute.standard.SheetCollate;
import javax.print.attribute.standard.Sides;
import javax.print.event.PrintJobAttributeEvent;
import javax.print.event.PrintJobAttributeListener;
import javax.print.event.PrintJobEvent;
import javax.print.event.PrintJobListener;
import javax.print.event.PrintServiceAttributeEvent;
import javax.print.event.PrintServiceAttributeListener;



public class HelloPrinter {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrintRequestAttributeSet requestAttributeSet = new HashPrintRequestAttributeSet();
		requestAttributeSet.add(MediaSizeName.ISO_A4);
		requestAttributeSet.add(new Copies(4));
		requestAttributeSet.add(Sides.DUPLEX);
		
		
		PrintService[] services = PrintServiceLookup.lookupPrintServices(DocFlavor.INPUT_STREAM.PDF, requestAttributeSet);
		for (PrintService service1 : services) {
			System.out.println(service1);
		}
		PrintService service = services[0];
		
		
		
		service.addPrintServiceAttributeListener(new PrintServiceAttributeListener() {
			
			@Override
			public void attributeUpdate(PrintServiceAttributeEvent event) {
				PrintServiceAttributeSet serviceAttributeSet = event.getAttributes();
				StringBuilder s = new StringBuilder();
				s.append("PrintServiceAttributeEvent\n");
				for (Attribute attribute : serviceAttributeSet.toArray()) {
					PrintServiceAttribute printServiceAttribute = (PrintServiceAttribute)attribute;
					
					s.append(printServiceAttribute.getCategory().getName() + "/" + 
							printServiceAttribute.getName() + " = " + printServiceAttribute.toString() + "\n");
					
				}
				System.out.println(s.toString());
				
			}
		});
		
		FileInputStream inputStream;
		try {
			inputStream = new FileInputStream("blank.pdf");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return;
			
		}
		DocAttributeSet docAttributeSet = new HashDocAttributeSet();
		
		docAttributeSet.add(MediaSizeName.ISO_A4);
		docAttributeSet.add(Sides.DUPLEX);
		
		Doc doc = new SimpleDoc(inputStream, DocFlavor.INPUT_STREAM.PDF, docAttributeSet);
		
		DocPrintJob job = service.createPrintJob();
		
		PrintJobAttributeSet jobAttributeSet = new HashPrintJobAttributeSet();
		
		jobAttributeSet.add(Chromaticity.MONOCHROME); 
		jobAttributeSet.add(new Copies(1)); 
		jobAttributeSet.add(new DateTimeAtCompleted(new Date())); 
		jobAttributeSet.add(new DateTimeAtCreation(new Date())); 
		jobAttributeSet.add(new DateTimeAtProcessing(new Date()));
		jobAttributeSet.add(new Destination(URI.create("smb://SOMECOMP/SOMEMACH"))); 
		jobAttributeSet.add(Fidelity.FIDELITY_FALSE); 
		jobAttributeSet.add(Finishings.NONE); 
		jobAttributeSet.add(new JobHoldUntil(new Date())); 
		jobAttributeSet.add(new JobImpressions(0)); 
		jobAttributeSet.add(new JobImpressionsCompleted(0)); 
		jobAttributeSet.add(new JobKOctets(0)); 
		jobAttributeSet.add(new JobKOctetsProcessed(0)); 
		jobAttributeSet.add(new JobMediaSheets(0)); 
		jobAttributeSet.add(new JobMediaSheetsCompleted(0)); 
		jobAttributeSet.add(new JobMessageFromOperator("", Locale.getDefault())); 
		jobAttributeSet.add(new JobName("", Locale.getDefault())); 
		jobAttributeSet.add(new JobOriginatingUserName("yuval", Locale.getDefault())); 
		jobAttributeSet.add(new JobPriority(1)); 
		jobAttributeSet.add(JobSheets.NONE); 
		jobAttributeSet.add(JobState.UNKNOWN); 
		jobAttributeSet.add(new JobStateReasons(0, 1)); 
		jobAttributeSet.add(MediaSizeName.ISO_A4); 
		jobAttributeSet.add( new MediaPrintableArea(0,0,1,1,1)); 
		jobAttributeSet.add(MultipleDocumentHandling.SINGLE_DOCUMENT); 
		jobAttributeSet.add(new NumberOfDocuments(0)); 
		jobAttributeSet.add(new NumberOfInterveningJobs(0)); 
		jobAttributeSet.add(new NumberUp(1)); 
		jobAttributeSet.add(OrientationRequested.PORTRAIT); 
		jobAttributeSet.add(new OutputDeviceAssigned("", Locale.getDefault())); 
		jobAttributeSet.add(new PageRanges(1)); 
		jobAttributeSet.add(PresentationDirection.TOBOTTOM_TORIGHT); 
		jobAttributeSet.add(new PrinterResolution(100, 100, PrinterResolution.DPI)); 
		jobAttributeSet.add(PrintQuality.NORMAL); 
		jobAttributeSet.add(SheetCollate.UNCOLLATED); 
		jobAttributeSet.add(Sides.ONE_SIDED);
	
		job.addPrintJobAttributeListener(new PrintJobAttributeListener() {
			
			@Override
			public void attributeUpdate(PrintJobAttributeEvent event) {
				PrintJobAttributeSet jobAttributeSet = event.getAttributes();
				StringBuilder s = new StringBuilder();
				s.append("PrintJobAttributeEvent\n");
				for (Attribute attribute : jobAttributeSet.toArray()) {
					PrintJobAttribute jobAttribute = (PrintJobAttribute)attribute;
					
					s.append(jobAttribute.getCategory().getName() + "/" + 
							jobAttribute.getName() + " = " + jobAttribute.toString() + "\n");
					
				}
				System.out.println(s.toString());
				
			}
		}, null);
		
		job.addPrintJobListener(new PrintJobListener() {
			
			@Override
			public void printJobRequiresAttention(PrintJobEvent pje) {
				System.out.println("printJobRequiresAttention");
				
			}
			
			@Override
			public void printJobNoMoreEvents(PrintJobEvent pje) {
				// TODO Auto-generated method stub
				System.out.println("PrintJobEvent: printJobNoMoreEvents");
 				System.out.println(pje.getPrintEventType());
 				System.out.println(pje.toString());
				
			}
			
			@Override
			public void printJobFailed(PrintJobEvent pje) {
				// TODO Auto-generated method stub
				System.out.println("printJobFailed");
 				System.out.println(pje.getPrintEventType());
 				System.out.println(pje.toString());
				
			}
			
			@Override
			public void printJobCompleted(PrintJobEvent pje) {
				// TODO Auto-generated method stub
				System.out.println("printJobCompleted");
 				System.out.println(pje.getPrintEventType());
 				System.out.println(pje.toString());
				
			}
			
			@Override
			public void printJobCanceled(PrintJobEvent pje) {
				// TODO Auto-generated method stub
				System.out.println("printJobCanceled");
 				System.out.println(pje.getPrintEventType());
 				System.out.println(pje.toString());
				
			}
			
			@Override
			public void printDataTransferCompleted(PrintJobEvent pje) {
				// TODO Auto-generated method stub
				System.out.println("printDataTransferCompleted");
 				System.out.println(pje.getPrintEventType());
 				System.out.println(pje.toString());
				
			}
		});
		
		try {
			job.print(doc, requestAttributeSet);
		} catch (PrintException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		while (true) {
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return;
			}
			System.out.println("I'm alive and it's " + new Date());
			System.out.println("Job attributes");
			for (Attribute attribute : job.getAttributes().toArray()) {
				System.out.println((attribute.getCategory().getName() + "/" + 
						attribute.getName() + " = " + attribute.toString() + "\n"));
			}
			System.out.println("Service attributes");
			for (Attribute attribute : service.getAttributes().toArray()) {
				System.out.println((attribute.getCategory().getName() + "/" + 
						attribute.getName() + " = " + attribute.toString() + "\n"));
			}
		}
	}

}