from tkinter import *
from tkinter import ttk
from datetime import *
from xlsxwriter import *
from LN_info import info
import openpyxl

class BarcodeAssistant:
	def __init__(self, window):
        # Initializations 
		self.wind = window
		self.wind.title('Barcode Assistant')
		self.wind.geometry('670x710')
		self.wind.resizable(False, False)

		#-------------------------------------
		# Left column (messages and Pallets inputs)
		#-------------------------------------
		frame_column_1 = LabelFrame(self.wind, borderwidth = '0')
		frame_column_1.place(x=10, y=0, width=300, height=360)

		#-------------------------------------
		# Message frame
		#-------------------------------------
		frame_msg = LabelFrame(frame_column_1, text = 'Message')
		frame_msg.place(x=0, y=0, relwidth=.99, height=55)

		self.message = Label(frame_msg, text = 'No message')
		self.message.place(x = 10, y = 4)

		#-------------------------------------
		# Information frame
		#-------------------------------------
		self.inputs_checked = False

		frame_info = LabelFrame(frame_column_1, text = 'Information')
		frame_info.place(x=0, y=57, relwidth=.99, height=115)

		Label(frame_info, text = 'Packaging date [dd/mm/yyyy]:').place(x = 5, y = 3)
		self.entry_day = Entry(frame_info, width = 4)
		self.entry_month = Entry(frame_info, width = 4)
		self.entry_year = Entry(frame_info, width = 7)

		self.entry_day.place(x = 177, y = 4)
		self.entry_month.place(x = 208, y = 4)
		self.entry_year.place(x = 240, y = 4)

		Label(frame_info, text = 'Reference number:').place(x = 5, y = 30)
		self.ref_number = Entry(frame_info, width = 28)
		self.ref_number.place(x = 115, y = 31)

		frame_save_button = LabelFrame(frame_info, pady = 7, bd = 0)
		frame_save_button.place(x = 10, y = 54)

		Button(frame_save_button, text = 'Save', relief="solid", bg = '#D3D3D3', bd = 1, width = 10, command = lambda: self.parameters(self.entry_day.get(), self.entry_month.get(), self.entry_year.get(), self.ref_number.get())).grid(row = 0, column = 0)

		Button(frame_column_1, text = 'Generate barcodes', relief="solid", fg='black', bg = '#95CB78', font=("Arial",8,"bold"), bd = 1, width = 26, height = 2, command = lambda: self.barcodes_information(
			self.entry_day.get(),self.entry_month.get(),self.entry_year.get(),self.ref_number.get(),
			
			self.fp_flat_parsley_1.get(),self.fp_flat_parsley_2.get(),self.fp_flat_parsley_3.get(),self.fp_flat_parsley_4.get(),
			self.fp_sage_1.get(),self.fp_sage_2.get(),self.fp_sage_3.get(),self.fp_sage_4.get(),
			self.fp_dill_1.get(),self.fp_dill_2.get(),self.fp_dill_3.get(),self.fp_dill_4.get(),
			self.fp_italian_basil_1.get(),self.fp_italian_basil_2.get(),self.fp_italian_basil_3.get(),self.fp_italian_basil_4.get(),
			self.fp_curly_parsley_1.get(),self.fp_curly_parsley_2.get(),self.fp_curly_parsley_3.get(),self.fp_curly_parsley_4.get(),
			self.fp_flat_coriander_1.get(),self.fp_flat_coriander_2.get(),self.fp_flat_coriander_3.get(),self.fp_flat_coriander_4.get(),
			self.fp_green_mint_1.get(),self.fp_green_mint_2.get(),self.fp_green_mint_3.get(),self.fp_green_mint_4.get(),
			self.fp_thyme_1.get(),self.fp_thyme_2.get(),self.fp_thyme_3.get(),self.fp_thyme_4.get(),
			self.fp_rosemary_1.get(),self.fp_rosemary_2.get(),self.fp_rosemary_3.get(),self.fp_rosemary_4.get(),
			
			self.pots_italian_basil_1.get(),self.pots_italian_basil_2.get(),self.pots_italian_basil_3.get(),self.pots_italian_basil_4.get(),self.pots_italian_basil_5.get(),self.pots_italian_basil_6.get(),self.pots_italian_basil_7.get(),self.pots_italian_basil_8.get(),self.pots_italian_basil_9.get(),self.pots_italian_basil_10.get(),self.pots_italian_basil_11.get(),self.pots_italian_basil_12.get(),self.pots_italian_basil_13.get(),self.pots_italian_basil_14.get(),self.pots_italian_basil_15.get(),self.pots_italian_basil_16.get(),self.pots_italian_basil_17.get(),
			self.pots_flat_coriander_1.get(),self.pots_flat_coriander_2.get(),self.pots_flat_coriander_3.get(),self.pots_flat_coriander_4.get(),self.pots_flat_coriander_5.get(),self.pots_flat_coriander_6.get(),self.pots_flat_coriander_7.get(),self.pots_flat_coriander_8.get(),self.pots_flat_coriander_9.get(),self.pots_flat_coriander_10.get(),self.pots_flat_coriander_11.get(),self.pots_flat_coriander_12.get(),self.pots_flat_coriander_13.get(),self.pots_flat_coriander_14.get(),self.pots_flat_coriander_15.get(),self.pots_flat_coriander_16.get(),self.pots_flat_coriander_17.get(),
			self.pots_thyme_1.get(),self.pots_thyme_2.get(),self.pots_thyme_3.get(),self.pots_thyme_4.get(),self.pots_thyme_5.get(),self.pots_thyme_6.get(),self.pots_thyme_7.get(),self.pots_thyme_8.get(),self.pots_thyme_9.get(),self.pots_thyme_10.get(),self.pots_thyme_11.get(),self.pots_thyme_12.get(),self.pots_thyme_13.get(),self.pots_thyme_14.get(),self.pots_thyme_15.get(),self.pots_thyme_16.get(),self.pots_thyme_17.get(),
			self.pots_green_mint_1.get(),self.pots_green_mint_2.get(),self.pots_green_mint_3.get(),self.pots_green_mint_4.get(),self.pots_green_mint_5.get(),self.pots_green_mint_6.get(),self.pots_green_mint_7.get(),self.pots_green_mint_8.get(),self.pots_green_mint_9.get(),self.pots_green_mint_10.get(),self.pots_green_mint_11.get(),self.pots_green_mint_12.get(),self.pots_green_mint_13.get(),self.pots_green_mint_14.get(),self.pots_green_mint_15.get(),self.pots_green_mint_16.get(),self.pots_green_mint_17.get(),
			self.pots_rosemary_1.get(),self.pots_rosemary_2.get(),self.pots_rosemary_3.get(),self.pots_rosemary_4.get(),self.pots_rosemary_5.get(),self.pots_rosemary_6.get(),self.pots_rosemary_7.get(),self.pots_rosemary_8.get(),self.pots_rosemary_9.get(),self.pots_rosemary_10.get(),self.pots_rosemary_11.get(),self.pots_rosemary_12.get(),self.pots_rosemary_13.get(),self.pots_rosemary_14.get(),self.pots_rosemary_15.get(),self.pots_rosemary_16.get(),self.pots_rosemary_17.get(),
			self.pots_chervil_1.get(),self.pots_chervil_2.get(),self.pots_chervil_3.get(),self.pots_chervil_4.get(),self.pots_chervil_5.get(),self.pots_chervil_6.get(),self.pots_chervil_7.get(),self.pots_chervil_8.get(),self.pots_chervil_9.get(),self.pots_chervil_10.get(),self.pots_chervil_11.get(),self.pots_chervil_12.get(),self.pots_chervil_13.get(),self.pots_chervil_14.get(),self.pots_chervil_15.get(),self.pots_chervil_16.get(),self.pots_chervil_17.get(),
			self.pots_watercress_1.get(),self.pots_watercress_2.get(),self.pots_watercress_3.get(),self.pots_watercress_4.get(),self.pots_watercress_5.get(),self.pots_watercress_6.get(),self.pots_watercress_7.get(),self.pots_watercress_8.get(),self.pots_watercress_9.get(),self.pots_watercress_10.get(),self.pots_watercress_11.get(),self.pots_watercress_12.get(),self.pots_watercress_13.get(),self.pots_watercress_14.get(),self.pots_watercress_15.get(),self.pots_watercress_16.get(),self.pots_watercress_17.get(),
			self.pots_melissa_1.get(),self.pots_melissa_2.get(),self.pots_melissa_3.get(),self.pots_melissa_4.get(),self.pots_melissa_5.get(),self.pots_melissa_6.get(),self.pots_melissa_7.get(),self.pots_melissa_8.get(),self.pots_melissa_9.get(),self.pots_melissa_10.get(),self.pots_melissa_11.get(),self.pots_melissa_12.get(),self.pots_melissa_13.get(),self.pots_melissa_14.get(),self.pots_melissa_15.get(),self.pots_melissa_16.get(),self.pots_melissa_17.get(),
			self.pots_oregano_1.get(),self.pots_oregano_2.get(),self.pots_oregano_3.get(),self.pots_oregano_4.get(),self.pots_oregano_5.get(),self.pots_oregano_6.get(),self.pots_oregano_7.get(),self.pots_oregano_8.get(),self.pots_oregano_9.get(),self.pots_oregano_10.get(),self.pots_oregano_11.get(),self.pots_oregano_12.get(),self.pots_oregano_13.get(),self.pots_oregano_14.get(),self.pots_oregano_15.get(),self.pots_oregano_16.get(),self.pots_oregano_17.get(),
			self.pots_flat_parsley_1.get(),self.pots_flat_parsley_2.get(),self.pots_flat_parsley_3.get(),self.pots_flat_parsley_4.get(),self.pots_flat_parsley_5.get(),self.pots_flat_parsley_6.get(),self.pots_flat_parsley_7.get(),self.pots_flat_parsley_8.get(),self.pots_flat_parsley_9.get(),self.pots_flat_parsley_10.get(),self.pots_flat_parsley_11.get(),self.pots_flat_parsley_12.get(),self.pots_flat_parsley_13.get(),self.pots_flat_parsley_14.get(),self.pots_flat_parsley_15.get(),self.pots_flat_parsley_16.get(),self.pots_flat_parsley_17.get(),
			self.pots_pea_shoots_1.get(),self.pots_pea_shoots_2.get(),self.pots_pea_shoots_3.get(),self.pots_pea_shoots_4.get(),self.pots_pea_shoots_5.get(),self.pots_pea_shoots_6.get(),self.pots_pea_shoots_7.get(),self.pots_pea_shoots_8.get(),self.pots_pea_shoots_9.get(),self.pots_pea_shoots_10.get(),self.pots_pea_shoots_11.get(),self.pots_pea_shoots_12.get(),self.pots_pea_shoots_13.get(),self.pots_pea_shoots_14.get(),self.pots_pea_shoots_15.get(),self.pots_pea_shoots_16.get(),self.pots_pea_shoots_17.get()
		)).place(x = 0, y = 176)

		Button(frame_column_1, text = 'Clear entries', relief="solid", bg = '#D3D3D3', font=("Arial",8,"bold"), bd = 1, width = 13, height = 2, command= lambda: self.clear()).place(x = 196, y = 176)

		#-------------------------------------
		# General information
		#-------------------------------------
		frame_info = LabelFrame(frame_column_1, text = 'Steps')
		frame_info.place(x=0, y=220, relwidth=.99, height=130)

		self.info_msg_1 = Label(frame_info, text = '1. Save packaging date and reference number')
		self.info_msg_1.place(x = 10, y = 4)

		self.info_msg_2 = Label(frame_info, text = '2. Complete quantities. Use more columns only if')
		self.info_msg_2.place(x = 10, y = 24)

		self.info_msg_3 = Label(frame_info, text = 'there is more than one pallet')
		self.info_msg_3.place(x = 23, y = 42)

		self.info_msg_4 = Label(frame_info, text = '3. Click on "Generate barcodes"')
		self.info_msg_4.place(x = 10, y = 62)

		self.info_msg_5 = Label(frame_info, text = '4. Open "MainBarcode.btw", refresh and Print PDF')
		self.info_msg_5.place(x = 10, y = 82)

		#-------------------------------------
		# Packaging column
		#-------------------------------------

		frames_height = 350
		ts_fp_frame_width = 320
		ts_fp_gray_width = 135
		
		frame_column_2 = LabelFrame(self.wind, borderwidth = '0')
		frame_column_2.place(x=314, y=0, width=1000, height=1020)

		# FLOWPACK

		frame_flowpack = LabelFrame(frame_column_2, text = 'Flowpack', font=("Arial",11,"bold"))
		frame_flowpack.place(x=0, y=0, width=347, height=frames_height)

		LabelFrame(frame_flowpack, borderwidth='0', bg='#D3D3D3').place(x = 195, y = 0, width=ts_fp_gray_width, height=280)
		Label(frame_flowpack, text = 'Pallet (1,2,3,4)', bg='#D3D3D3', font=("Arial",8,"bold")).place(x=224,y=2)

		fp_x = 202
		fp_y = 24
		step_x = 31
		step_y = 27

		Label(frame_flowpack, text = 'Flowpack - Flat Parsley (Pr26)').place(x = 5, y = fp_y-1)
		self.fp_flat_parsley_1 = Entry(frame_flowpack, width = 4)
		self.fp_flat_parsley_2 = Entry(frame_flowpack, width = 4)
		self.fp_flat_parsley_3 = Entry(frame_flowpack, width = 4)
		self.fp_flat_parsley_4 = Entry(frame_flowpack, width = 4)
		self.fp_flat_parsley_1.place(x = fp_x, y = fp_y)
		self.fp_flat_parsley_2.place(x = fp_x+step_x, y = fp_y)
		self.fp_flat_parsley_3.place(x = fp_x+step_x*2, y = fp_y)
		self.fp_flat_parsley_4.place(x = fp_x+step_x*3, y = fp_y)

		Label(frame_flowpack, text = 'Flowpack - Sage (Sg2)').place(x = 5, y = fp_y-1+step_y*1)
		self.fp_sage_1 = Entry(frame_flowpack, width = 4)
		self.fp_sage_2 = Entry(frame_flowpack, width = 4)
		self.fp_sage_3 = Entry(frame_flowpack, width = 4)
		self.fp_sage_4 = Entry(frame_flowpack, width = 4)
		self.fp_sage_1.place(x = fp_x, y = fp_y+step_y*1)
		self.fp_sage_2.place(x = fp_x+step_x, y = fp_y+step_y*1)
		self.fp_sage_3.place(x = fp_x+step_x*2, y = fp_y+step_y*1)
		self.fp_sage_4.place(x = fp_x+step_x*3, y = fp_y+step_y*1)

		Label(frame_flowpack, text = 'Flowpack - Dill (Dl6)').place(x = 5, y = fp_y-1+step_y*2)
		self.fp_dill_1 = Entry(frame_flowpack, width = 4)
		self.fp_dill_2 = Entry(frame_flowpack, width = 4)
		self.fp_dill_3 = Entry(frame_flowpack, width = 4)
		self.fp_dill_4 = Entry(frame_flowpack, width = 4)
		self.fp_dill_1.place(x = fp_x, y = fp_y+step_y*2)
		self.fp_dill_2.place(x = fp_x+step_x, y = fp_y+step_y*2)
		self.fp_dill_3.place(x = fp_x+step_x*2, y = fp_y+step_y*2)
		self.fp_dill_4.place(x = fp_x+step_x*3, y = fp_y+step_y*2)

		Label(frame_flowpack, text = 'Flowpack - Italian Basil (Bs49)').place(x = 5, y = fp_y-1+step_y*3)
		self.fp_italian_basil_1 = Entry(frame_flowpack, width = 4)
		self.fp_italian_basil_2 = Entry(frame_flowpack, width = 4)
		self.fp_italian_basil_3 = Entry(frame_flowpack, width = 4)
		self.fp_italian_basil_4 = Entry(frame_flowpack, width = 4)
		self.fp_italian_basil_1.place(x = fp_x, y = fp_y+step_y*3)
		self.fp_italian_basil_2.place(x = fp_x+step_x, y = fp_y+step_y*3)
		self.fp_italian_basil_3.place(x = fp_x+step_x*2, y = fp_y+step_y*3)
		self.fp_italian_basil_4.place(x = fp_x+step_x*3, y = fp_y+step_y*3)
		
		Label(frame_flowpack, text = 'Flowpack - Curly Parsley (Pr21)').place(x = 5, y = fp_y-1+step_y*4)
		self.fp_curly_parsley_1 = Entry(frame_flowpack, width = 4)
		self.fp_curly_parsley_2 = Entry(frame_flowpack, width = 4)
		self.fp_curly_parsley_3 = Entry(frame_flowpack, width = 4)
		self.fp_curly_parsley_4 = Entry(frame_flowpack, width = 4)
		self.fp_curly_parsley_1.place(x = fp_x, y = fp_y+step_y*4)
		self.fp_curly_parsley_2.place(x = fp_x + step_x, y = fp_y+step_y*4)
		self.fp_curly_parsley_3.place(x = fp_x + step_x*2, y = fp_y+step_y*4)
		self.fp_curly_parsley_4.place(x = fp_x + step_x*3, y = fp_y+step_y*4)

		Label(frame_flowpack, text = 'Flowpack - Flat Coriander (Cr26)').place(x = 5, y = fp_y-1+step_y*5)
		self.fp_flat_coriander_1 = Entry(frame_flowpack, width = 4)
		self.fp_flat_coriander_2 = Entry(frame_flowpack, width = 4)
		self.fp_flat_coriander_3 = Entry(frame_flowpack, width = 4)
		self.fp_flat_coriander_4 = Entry(frame_flowpack, width = 4)
		self.fp_flat_coriander_1.place(x = fp_x, y = fp_y+step_y*5)
		self.fp_flat_coriander_2.place(x = fp_x + step_x, y = fp_y+step_y*5)
		self.fp_flat_coriander_3.place(x = fp_x + step_x*2, y = fp_y+step_y*5)
		self.fp_flat_coriander_4.place(x = fp_x + step_x*3, y = fp_y+step_y*5)

		Label(frame_flowpack, text = 'Flowpack - Green Mint (Mn3)').place(x = 5, y = fp_y-1+step_y*6)
		self.fp_green_mint_1 = Entry(frame_flowpack, width = 4)
		self.fp_green_mint_2 = Entry(frame_flowpack, width = 4)
		self.fp_green_mint_3 = Entry(frame_flowpack, width = 4)
		self.fp_green_mint_4 = Entry(frame_flowpack, width = 4)
		self.fp_green_mint_1.place(x = fp_x, y = fp_y+step_y*6)
		self.fp_green_mint_2.place(x = fp_x + step_x, y = fp_y+step_y*6)
		self.fp_green_mint_3.place(x = fp_x + step_x*2, y = fp_y+step_y*6)
		self.fp_green_mint_4.place(x = fp_x + step_x*3, y = fp_y+step_y*6)

		Label(frame_flowpack, text = 'Flowpack - Thyme (Tm5)').place(x = 5, y = fp_y-1+step_y*7)
		self.fp_thyme_1 = Entry(frame_flowpack, width = 4)
		self.fp_thyme_2 = Entry(frame_flowpack, width = 4)
		self.fp_thyme_3 = Entry(frame_flowpack, width = 4)
		self.fp_thyme_4 = Entry(frame_flowpack, width = 4)
		self.fp_thyme_1.place(x = fp_x, y = fp_y+step_y*7)
		self.fp_thyme_2.place(x = fp_x + step_x, y = fp_y+step_y*7)
		self.fp_thyme_3.place(x = fp_x + step_x*2, y = fp_y+step_y*7)
		self.fp_thyme_4.place(x = fp_x + step_x*3, y = fp_y+step_y*7)

		Label(frame_flowpack, text = 'Flowpack - Rosemary (Rs4)').place(x = 5, y = fp_y-1+step_y*8)
		self.fp_rosemary_1 = Entry(frame_flowpack, width = 4)
		self.fp_rosemary_2 = Entry(frame_flowpack, width = 4)
		self.fp_rosemary_3 = Entry(frame_flowpack, width = 4)
		self.fp_rosemary_4 = Entry(frame_flowpack, width = 4)
		self.fp_rosemary_1.place(x = fp_x, y = fp_y+step_y*8)
		self.fp_rosemary_2.place(x = fp_x + step_x, y = fp_y+step_y*8)
		self.fp_rosemary_3.place(x = fp_x + step_x*2, y = fp_y+step_y*8)
		self.fp_rosemary_4.place(x = fp_x + step_x*3, y = fp_y+step_y*8)

		# POTS

		frame_pots = LabelFrame(self.wind, text = 'Pots', font=("Arial",11,"bold"))
		frame_pots.place(x=10, y=350, width=320*2.035, height=frames_height)

		LabelFrame(frame_pots, borderwidth='0', bg='#D3D3D3').place(x = 210, y = 0, width=431, height=325)

		for i in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']:
			Label(frame_pots, text = f'({i})', bg='#D3D3D3', font=("Arial",7,"bold")).place(x=213+25*(int(i)-1),y=4)

		pots_x = 213
		pots_y = 24
		pots_width = 3
		step_x_pots = 25
		step_y = 27
		Label(frame_pots, text = 'Pots - Italiensk Basilikum (It. Basil)').place(x = 5, y = pots_y-1)
		self.pots_italian_basil_1 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_2 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_3 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_4 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_5 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_6 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_7 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_8 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_9 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_10 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_11 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_12 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_13 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_14 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_15 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_16 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_17 = Entry(frame_pots, width = pots_width)
		self.pots_italian_basil_1.place(x = pots_x, y = pots_y)
		self.pots_italian_basil_2.place(x = pots_x+step_x_pots, y = pots_y)
		self.pots_italian_basil_3.place(x = pots_x+step_x_pots*2, y = pots_y)
		self.pots_italian_basil_4.place(x = pots_x+step_x_pots*3, y = pots_y)
		self.pots_italian_basil_5.place(x = pots_x+step_x_pots*4, y = pots_y)
		self.pots_italian_basil_6.place(x = pots_x+step_x_pots*5, y = pots_y)
		self.pots_italian_basil_7.place(x = pots_x+step_x_pots*6, y = pots_y)
		self.pots_italian_basil_8.place(x = pots_x+step_x_pots*7, y = pots_y)
		self.pots_italian_basil_9.place(x = pots_x+step_x_pots*8, y = pots_y)
		self.pots_italian_basil_10.place(x = pots_x+step_x_pots*9, y = pots_y)
		self.pots_italian_basil_11.place(x = pots_x+step_x_pots*10, y = pots_y)
		self.pots_italian_basil_12.place(x = pots_x+step_x_pots*11, y = pots_y)
		self.pots_italian_basil_13.place(x = pots_x+step_x_pots*12, y = pots_y)
		self.pots_italian_basil_14.place(x = pots_x+step_x_pots*13, y = pots_y)
		self.pots_italian_basil_15.place(x = pots_x+step_x_pots*14, y = pots_y)
		self.pots_italian_basil_16.place(x = pots_x+step_x_pots*15, y = pots_y)
		self.pots_italian_basil_17.place(x = pots_x+step_x_pots*16, y = pots_y)

		Label(frame_pots, text = 'Pots - Koriander (Flat Coriander)').place(x = 5, y = pots_y-1+step_y*1)
		self.pots_flat_coriander_1 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_2 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_3 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_4 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_5 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_6 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_7 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_8 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_9 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_10 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_11 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_12 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_13 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_14 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_15 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_16 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_17 = Entry(frame_pots, width = pots_width)
		self.pots_flat_coriander_1.place(x = pots_x, y = pots_y+step_y*1)
		self.pots_flat_coriander_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*1)
		self.pots_flat_coriander_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*1)
		self.pots_flat_coriander_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*1)
		self.pots_flat_coriander_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*1)
		self.pots_flat_coriander_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*1)
		self.pots_flat_coriander_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*1)
		self.pots_flat_coriander_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*1)
		self.pots_flat_coriander_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*1)
		self.pots_flat_coriander_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*1)
		self.pots_flat_coriander_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*1)
		self.pots_flat_coriander_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*1)
		self.pots_flat_coriander_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*1)
		self.pots_flat_coriander_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*1)
		self.pots_flat_coriander_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*1)
		self.pots_flat_coriander_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*1)
		self.pots_flat_coriander_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*1)

		Label(frame_pots, text = 'Pots - Timian (Thyme)').place(x = 5, y = pots_y-1+step_y*2)
		self.pots_thyme_1 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_2 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_3 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_4 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_5 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_6 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_7 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_8 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_9 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_10 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_11 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_12 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_13 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_14 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_15 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_16 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_17 = Entry(frame_pots, width = pots_width)
		self.pots_thyme_1.place(x = pots_x, y = pots_y+step_y*2)
		self.pots_thyme_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*2)
		self.pots_thyme_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*2)
		self.pots_thyme_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*2)
		self.pots_thyme_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*2)
		self.pots_thyme_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*2)
		self.pots_thyme_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*2)
		self.pots_thyme_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*2)
		self.pots_thyme_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*2)
		self.pots_thyme_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*2)
		self.pots_thyme_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*2)
		self.pots_thyme_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*2)
		self.pots_thyme_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*2)
		self.pots_thyme_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*2)
		self.pots_thyme_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*2)
		self.pots_thyme_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*2)
		self.pots_thyme_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*2)

		Label(frame_pots, text = 'Pots - Pebermynte (Peppermint)').place(x = 5, y = pots_y-1+step_y*3)
		self.pots_green_mint_1 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_2 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_3 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_4 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_5 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_6 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_7 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_8 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_9 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_10 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_11 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_12 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_13 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_14 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_15 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_16 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_17 = Entry(frame_pots, width = pots_width)
		self.pots_green_mint_1.place(x = pots_x, y = pots_y+step_y*3)
		self.pots_green_mint_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*3)
		self.pots_green_mint_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*3)
		self.pots_green_mint_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*3)
		self.pots_green_mint_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*3)
		self.pots_green_mint_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*3)
		self.pots_green_mint_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*3)
		self.pots_green_mint_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*3)
		self.pots_green_mint_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*3)
		self.pots_green_mint_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*3)
		self.pots_green_mint_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*3)
		self.pots_green_mint_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*3)
		self.pots_green_mint_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*3)
		self.pots_green_mint_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*3)
		self.pots_green_mint_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*3)
		self.pots_green_mint_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*3)
		self.pots_green_mint_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*3)

		Label(frame_pots, text = 'Pots - Rosmarin (Rosemary)').place(x = 5, y = pots_y-1+step_y*4)
		self.pots_rosemary_1 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_2 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_3 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_4 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_5 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_6 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_7 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_8 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_9 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_10 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_11 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_12 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_13 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_14 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_15 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_16 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_17 = Entry(frame_pots, width = pots_width)
		self.pots_rosemary_1.place(x = pots_x, y = pots_y+step_y*4)
		self.pots_rosemary_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*4)
		self.pots_rosemary_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*4)
		self.pots_rosemary_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*4)
		self.pots_rosemary_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*4)
		self.pots_rosemary_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*4)
		self.pots_rosemary_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*4)
		self.pots_rosemary_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*4)
		self.pots_rosemary_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*4)
		self.pots_rosemary_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*4)
		self.pots_rosemary_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*4)
		self.pots_rosemary_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*4)
		self.pots_rosemary_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*4)
		self.pots_rosemary_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*4)
		self.pots_rosemary_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*4)
		self.pots_rosemary_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*4)
		self.pots_rosemary_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*4)

		Label(frame_pots, text = 'Pots - Kørvel (Chervil)').place(x = 5, y = pots_y-1+step_y*5)
		self.pots_chervil_1 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_2 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_3 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_4 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_5 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_6 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_7 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_8 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_9 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_10 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_11 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_12 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_13 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_14 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_15 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_16 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_17 = Entry(frame_pots, width = pots_width)
		self.pots_chervil_1.place(x = pots_x, y = pots_y+step_y*5)
		self.pots_chervil_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*5)
		self.pots_chervil_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*5)
		self.pots_chervil_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*5)
		self.pots_chervil_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*5)
		self.pots_chervil_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*5)
		self.pots_chervil_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*5)
		self.pots_chervil_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*5)
		self.pots_chervil_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*5)
		self.pots_chervil_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*5)
		self.pots_chervil_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*5)
		self.pots_chervil_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*5)
		self.pots_chervil_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*5)
		self.pots_chervil_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*5)
		self.pots_chervil_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*5)
		self.pots_chervil_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*5)
		self.pots_chervil_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*5)

		Label(frame_pots, text = 'Pots - Brøndkarse (Watercress)').place(x = 5, y = pots_y-1+step_y*6)
		self.pots_watercress_1 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_2 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_3 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_4 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_5 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_6 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_7 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_8 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_9 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_10 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_11 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_12 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_13 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_14 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_15 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_16 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_17 = Entry(frame_pots, width = pots_width)
		self.pots_watercress_1.place(x = pots_x, y = pots_y+step_y*6)
		self.pots_watercress_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*6)
		self.pots_watercress_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*6)
		self.pots_watercress_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*6)
		self.pots_watercress_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*6)
		self.pots_watercress_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*6)
		self.pots_watercress_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*6)
		self.pots_watercress_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*6)
		self.pots_watercress_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*6)
		self.pots_watercress_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*6)
		self.pots_watercress_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*6)
		self.pots_watercress_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*6)
		self.pots_watercress_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*6)
		self.pots_watercress_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*6)
		self.pots_watercress_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*6)
		self.pots_watercress_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*6)
		self.pots_watercress_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*6)

		Label(frame_pots, text = 'Pots - Citronmellisse (Melissa)').place(x = 5, y = pots_y-1+step_y*7)
		self.pots_melissa_1 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_2 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_3 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_4 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_5 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_6 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_7 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_8 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_9 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_10 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_11 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_12 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_13 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_14 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_15 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_16 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_17 = Entry(frame_pots, width = pots_width)
		self.pots_melissa_1.place(x = pots_x, y = pots_y+step_y*7)
		self.pots_melissa_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*7)
		self.pots_melissa_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*7)
		self.pots_melissa_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*7)
		self.pots_melissa_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*7)
		self.pots_melissa_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*7)
		self.pots_melissa_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*7)
		self.pots_melissa_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*7)
		self.pots_melissa_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*7)
		self.pots_melissa_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*7)
		self.pots_melissa_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*7)
		self.pots_melissa_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*7)
		self.pots_melissa_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*7)
		self.pots_melissa_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*7)
		self.pots_melissa_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*7)
		self.pots_melissa_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*7)
		self.pots_melissa_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*7)

		Label(frame_pots, text = 'Pots - Oregano (Oregano)').place(x = 5, y = pots_y-1+step_y*8)
		self.pots_oregano_1 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_2 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_3 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_4 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_5 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_6 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_7 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_8 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_9 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_10 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_11 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_12 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_13 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_14 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_15 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_16 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_17 = Entry(frame_pots, width = pots_width)
		self.pots_oregano_1.place(x = pots_x, y = pots_y+step_y*8)
		self.pots_oregano_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*8)
		self.pots_oregano_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*8)
		self.pots_oregano_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*8)
		self.pots_oregano_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*8)
		self.pots_oregano_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*8)
		self.pots_oregano_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*8)
		self.pots_oregano_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*8)
		self.pots_oregano_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*8)
		self.pots_oregano_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*8)
		self.pots_oregano_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*8)
		self.pots_oregano_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*8)
		self.pots_oregano_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*8)
		self.pots_oregano_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*8)
		self.pots_oregano_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*8)
		self.pots_oregano_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*8)
		self.pots_oregano_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*8)

		Label(frame_pots, text = 'Pots - Bredbladet Persille (F. Parsley)').place(x = 5, y = pots_y-1+step_y*9)
		self.pots_flat_parsley_1 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_2 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_3 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_4 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_5 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_6 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_7 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_8 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_9 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_10 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_11 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_12 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_13 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_14 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_15 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_16 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_17 = Entry(frame_pots, width = pots_width)
		self.pots_flat_parsley_1.place(x = pots_x, y = pots_y+step_y*9)
		self.pots_flat_parsley_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*9)
		self.pots_flat_parsley_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*9)
		self.pots_flat_parsley_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*9)
		self.pots_flat_parsley_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*9)
		self.pots_flat_parsley_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*9)
		self.pots_flat_parsley_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*9)
		self.pots_flat_parsley_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*9)
		self.pots_flat_parsley_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*9)
		self.pots_flat_parsley_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*9)
		self.pots_flat_parsley_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*9)
		self.pots_flat_parsley_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*9)
		self.pots_flat_parsley_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*9)
		self.pots_flat_parsley_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*9)
		self.pots_flat_parsley_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*9)
		self.pots_flat_parsley_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*9)
		self.pots_flat_parsley_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*9)

		Label(frame_pots, text = 'Pots - Ærteskud (Pea Shoots)').place(x = 5, y = pots_y-1+step_y*10)
		self.pots_pea_shoots_1 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_2 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_3 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_4 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_5 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_6 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_7 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_8 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_9 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_10 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_11 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_12 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_13 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_14 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_15 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_16 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_17 = Entry(frame_pots, width = pots_width)
		self.pots_pea_shoots_1.place(x = pots_x, y = pots_y+step_y*10)
		self.pots_pea_shoots_2.place(x = pots_x+step_x_pots, y = pots_y+step_y*10)
		self.pots_pea_shoots_3.place(x = pots_x+step_x_pots*2, y = pots_y+step_y*10)
		self.pots_pea_shoots_4.place(x = pots_x+step_x_pots*3, y = pots_y+step_y*10)
		self.pots_pea_shoots_5.place(x = pots_x+step_x_pots*4, y = pots_y+step_y*10)
		self.pots_pea_shoots_6.place(x = pots_x+step_x_pots*5, y = pots_y+step_y*10)
		self.pots_pea_shoots_7.place(x = pots_x+step_x_pots*6, y = pots_y+step_y*10)
		self.pots_pea_shoots_8.place(x = pots_x+step_x_pots*7, y = pots_y+step_y*10)
		self.pots_pea_shoots_9.place(x = pots_x+step_x_pots*8, y = pots_y+step_y*10)
		self.pots_pea_shoots_10.place(x = pots_x+step_x_pots*9, y = pots_y+step_y*10)
		self.pots_pea_shoots_11.place(x = pots_x+step_x_pots*10, y = pots_y+step_y*10)
		self.pots_pea_shoots_12.place(x = pots_x+step_x_pots*11, y = pots_y+step_y*10)
		self.pots_pea_shoots_13.place(x = pots_x+step_x_pots*12, y = pots_y+step_y*10)
		self.pots_pea_shoots_14.place(x = pots_x+step_x_pots*13, y = pots_y+step_y*10)
		self.pots_pea_shoots_15.place(x = pots_x+step_x_pots*14, y = pots_y+step_y*10)
		self.pots_pea_shoots_16.place(x = pots_x+step_x_pots*15, y = pots_y+step_y*10)
		self.pots_pea_shoots_17.place(x = pots_x+step_x_pots*16, y = pots_y+step_y*10)

	#-------------------------------------
	# Functions
	#-------------------------------------

	def parameters(self,day,month,year,ref_num):
		if ref_num != "" and len(year) == 4:
			try:
				date(int(year),int(month),int(day))
				if date(int(year),int(month),int(day)).weekday()+1 != 7: 
					self.message['text'] = "Inputs changed"
					self.message['fg'] = 'green'
					self.message['font'] = ('Helvetica', 8, 'bold')
					self.inputs_checked = True
				else:
					self.message['text'] = "Input date is Sunday"
					self.message['fg'] = 'red'
					self.message['font'] = ('Helvetica', 8, 'bold')
					self.inputs_checked = False
			except:
				self.message['text'] = "Please check/save inputs"
				self.message['fg'] = 'red'
				self.message['font'] = ('Helvetica', 8, 'bold')
				self.inputs_checked = False
		else:
			self.message['text'] = "Please check/save inputs"
			self.message['fg'] = 'red'
			self.message['font'] = ('Helvetica', 8, 'bold')
			self.inputs_checked = False

	def barcodes_information(self,dd,mm,yyyy,ref_number,
		fp1,fp2,fp3,fp4,fp5,fp6,fp7,fp8,fp9,fp10,fp11,fp12,fp13,fp14,
		fp15,fp16,fp17,fp18,fp19,fp20,fp21,fp22,fp23,fp24,fp25,fp26,fp27,fp28,fp29,fp30,fp31,fp32,fp33,fp34,fp35,fp36,
		p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,
		p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,p57,p58,p59,p60,
		p61,p62,p63,p64,p65,p66,p67,p68,p69,p70,p71,p72,p73,p74,p75,p76,p77,p78,p79,p80,p81,p82,p83,p84,p85,p86,p87,p88,p89,p90,
		p91,p92,p93,p94,p95,p96,p97,p98,p99,p100,p101,p102,p103,p104,p105,p106,p107,p108,p109,p110,p111,p112,p113,p114,p115,p116,p117,p118,p119,p120,
		p121,p122,p123,p124,p125,p126,p127,p128,p129,p130,p131,p132,p133,p134,p135,p136,p137,p138,p139,p140,p141,p142,p143,p144,p145,p146,p147,p148,p149,p150,
		p151,p152,p153,p154,p155,p156,p157,p158,p159,p160,p161,p162,p163,p164,p165,p166,p167,p168,p169,p170,p171,p172,p173,p174,p175,p176,
		p177,p178,p179,p180,p181,p182,p183,p184,p185,p186,p187
		):
		if self.inputs_checked == False or self.ref_number.get() == '':
			self.message['text'] = "Please check/save inputs"
			self.message['fg'] = 'red'
			self.message['font'] = ('Helvetica', 8, 'bold')
			self.inputs_checked = False
		else:
			try:
				quantities = [
							fp1,fp2,fp3,fp4,fp5,fp6,fp7,fp8,fp9,fp10,fp11,fp12,fp13,fp14,
							fp15,fp16,fp17,fp18,fp19,fp20,fp21,fp22,fp23,fp24,fp25,fp26,fp27,fp28,fp29,fp30,fp31,fp32,fp33,fp34,fp35,fp36,
							p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,
							p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,p57,p58,p59,p60,
							p61,p62,p63,p64,p65,p66,p67,p68,p69,p70,p71,p72,p73,p74,p75,p76,p77,p78,p79,p80,p81,p82,p83,p84,p85,p86,p87,p88,p89,p90,
							p91,p92,p93,p94,p95,p96,p97,p98,p99,p100,p101,p102,p103,p104,p105,p106,p107,p108,p109,p110,p111,p112,p113,p114,p115,p116,p117,p118,p119,p120,
							p121,p122,p123,p124,p125,p126,p127,p128,p129,p130,p131,p132,p133,p134,p135,p136,p137,p138,p139,p140,p141,p142,p143,p144,p145,p146,p147,p148,p149,p150,
							p151,p152,p153,p154,p155,p156,p157,p158,p159,p160,p161,p162,p163,p164,p165,p166,p167,p168,p169,p170,p171,p172,p173,p174,p175,p176,
							p177,p178,p179,p180,p181,p182,p183,p184,p185,p186,p187
							]

				varieties = [
							"Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley",
							"Sage","Sage","Sage","Sage",
							"Dill","Dill","Dill","Dill",
							"Italian Basil","Italian Basil","Italian Basil","Italian Basil",
							"Curly Parsley","Curly Parsley","Curly Parsley","Curly Parsley",
							"Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander",
							"Green Mint","Green Mint","Green Mint","Green Mint",
							"Thyme","Thyme","Thyme","Thyme",
							"Rosemary","Rosemary","Rosemary","Rosemary",
							"Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil","Italian Basil",
							"Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander","Flat Coriander",
							"Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme","Thyme",
							"Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint","Green Mint",
							"Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary","Rosemary",
							"Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil","Chervil",
							"Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress","Watercress",
							"Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa","Melissa",
							"Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano","Oregano",
							"Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley","Flat Parsley",
							"Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots","Pea Shoots"
							]

				all_info = []

				c = 0

				wb = openpyxl.load_workbook("PalletCounter.xlsx", data_only=True)
				sh = wb["Sheet1"]
				last_pallet = sh["A2"].value

				for item in quantities:
					if 0 <= c <= 35:
						process = "fp"
					else:
						process = "pots"

					if item != '':
						pallet = str((last_pallet+1)).zfill(5)
						last_pallet +=1
					else:
						pallet = ''

					item_info = info(int(dd),int(mm),int(yyyy),ref_number,process,varieties[c])
					
					all_info.append([item_info[0],item_info[1],item_info[2],item_info[3],varieties[c],process,quantities[c],pallet])
					
					c += 1

					packed = [item for item in all_info if item[6] != '' and item[6] != '0']

					row = 1

					self.workbook = Workbook('BarcodeInformation.xlsx')
					self.worksheet = self.workbook.add_worksheet("BarcodeData")

					headers = ["Best before", "Item ID", "Ref Number", "Batch/Lot", "Quantity", "Variety", "Barcode1", "Barcode1 (text)", "Barcode2", "Barcode2 (text)","Barcode3"]

					for i in range(len(headers)):
						self.worksheet.write(0,i,headers[i])
						self.worksheet.set_column(0, i, 15)

					for plant in packed:
						self.add_row(row, plant[0], plant[1], plant[2][2:4], plant[3], ref_number, plant[4], plant[5], plant[6], plant[7])
						row += 1

					self.workbook.close()

					self.message['text'] = "Barcodes data generated"
					self.message['fg'] = 'green'
					self.message['font'] = ('Helvetica', 8, 'bold')

				sh["A2"].value = last_pallet
				wb.save("PalletCounter.xlsx")
			except:
				self.message['text'] = "Please check/save inputs"
				self.message['fg'] = 'red'
				self.message['font'] = ('Helvetica', 8, 'bold')
									
	def add_row(self,j, dd, mm, yy, ln, ref_number, variety, process, quantity, pallet):

		item_ids = [{"Italian Basil":14260548675433, "Flat Coriander":14260548675457, "Thyme":14260548675464, "Green Mint":14260548677550, "Rosemary":14260548675471, "Chervil":14260548675501, "Tarragon":14260548675518, "Watercress":14260548675525, "Melissa":14260548675532, "Oregano":14260548677567, "Flat Parsley":14260548677581, "Pea Shoots":14260548677574},
				{"Italian Basil":14260548677055, "Flat Coriander":14260548675570, "Thyme":14260548675594, "Green Mint":14260548675587, "Rosemary":14260548675600, "Dill":14260548677062, "Tarragon":14260548675617, "Sage":14260548675624, "Curly Parsley":14260548675563, "Flat Parsley":14260548675556},
				{"Italian Basil":14260548675884, "Flat Coriander":14260548675839, "Thyme":14260548675853, "Green Mint":14260548675846, "Rosemary":14260548675860, "Curly Parsley":14260548675891, "Tarragon":14260548675617, "Flat Parsley":14260548677987, "Sage":14260548678007, "Dill":14260548677970}] #[pots,ts,fp]

		# Obsolete
		serial_nums = [{"Italian Basil":5433, "Flat Coriander":5457, "Thyme":5464, "Green Mint":7550, "Rosemary":5471, "Chervil":5501, "Tarragon":5518, "Watercress":5525, "Melissa":5532, "Oregano":7567, "Flat Parsley":7581, "Pea Shoots":7574},
					{"Italian Basil":7055, "Flat Coriander":5570, "Thyme":5594, "Green Mint":5587, "Rosemary":5600, "Dill":7062, "Tarragon":5617, "Sage":5624, "Curly Parsley":5563, "Flat Parsley":5556},
					{"Italian Basil":5884, "Flat Coriander":5839, "Thyme":5853, "Green Mint":5846, "Rosemary":5860, "Curly Parsley":5891, "Tarragon":5617, "Flat Parsley":7987, "Sage":8007, "Dill":7970}] #[pots,ts,fp]]

		variety_description = [{"Italian Basil":"Pots: Italiensk Basilikum", "Flat Coriander":"Pots: Koriander", "Thyme":"Pots: Timian", "Green Mint":"Pots: Pebermynte", "Rosemary":"Pots: Rosmarin", "Chervil":"Pots: Kørvel", "Tarragon":"Pots: Estragon", "Watercress":"Pots: Brøndkarse", "Melissa":"Pots: Citronmellisse", "Oregano":"Pots: Oregano", "Flat Parsley":"Pots: Bredbladet Persille", "Pea Shoots":"Pots: Ærteskud"},
					{"Italian Basil":"Tray seal: Italiensk Basilikum", "Flat Coriander":"Tray seal: Koriander", "Thyme":"Tray seal: Timian", "Green Mint":"Tray seal: Grøn Mint", "Rosemary":"Tray seal: Rosmarin", "Dill":"Tray seal: Dild", "Tarragon":"Tray seal: Estragon", "Sage":"Tray seal: Salvie", "Curly Parsley":"Tray seal: Kruspersille", "Flat Parsley":"Tray seal: Bredbladet Persille"},
					{"Italian Basil":"Flowpack: Italiensk Basilikum", "Flat Coriander":"Flowpack: Koriander", "Thyme":"Flowpack: Timian", "Green Mint":"Flowpack: Grøn Mint", "Rosemary":"Flowpack: Rosmarin", "Curly Parsley":"Flowpack: Kruspersille", "Tarragon":"Flowpack: Estragon", "Flat Parsley":"Flowpack: Bredbladet Persille", "Sage":"Flowpack: Salvie", "Dill":"Flowpack: Dild"}] #[pots,ts,fp]


		processes = {"pots":0,"ts":1,"fp":2}
		self.worksheet.write(j,0,f'{dd}/{mm}/{yy}')
		self.worksheet.write(j,1,f'INDHOLD: {item_ids[processes[process]][variety]}')
		self.worksheet.write(j,2,f'{ref_number}')
		self.worksheet.write(j,3,f'{ln}')
		self.worksheet.write(j,4,f'{quantity}')
		self.worksheet.write(j,5,f'{variety_description[processes[process]][variety]}')
		self.worksheet.write(j,6,f'02{item_ids[processes[process]][variety]}37{quantity}')
		self.worksheet.write(j,7,f'(02){item_ids[processes[process]][variety]}(37){quantity}')
		self.worksheet.write(j,8,f'15{yy+mm+dd}10{ln}400{ref_number}')
		self.worksheet.write(j,9,f'(15){yy+mm+dd}(10){ln}(400){ref_number}')
		self.worksheet.write(j,10,f'{pallet}')

	def clear(self):
		self.ref_number.delete(0,'end')

		self.fp_flat_parsley_1.delete(0,'end')
		self.fp_flat_parsley_2.delete(0,'end')
		self.fp_flat_parsley_3.delete(0,'end')
		self.fp_flat_parsley_4.delete(0,'end')	
		self.fp_sage_1.delete(0,'end')
		self.fp_sage_2.delete(0,'end')
		self.fp_sage_3.delete(0,'end')
		self.fp_sage_4.delete(0,'end')
		self.fp_dill_1.delete(0,'end')
		self.fp_dill_2.delete(0,'end')
		self.fp_dill_3.delete(0,'end')
		self.fp_dill_4.delete(0,'end')
		self.fp_italian_basil_1.delete(0,'end')
		self.fp_italian_basil_2.delete(0,'end')
		self.fp_italian_basil_3.delete(0,'end')
		self.fp_italian_basil_4.delete(0,'end')
		self.fp_curly_parsley_1.delete(0,'end')
		self.fp_curly_parsley_2.delete(0,'end')
		self.fp_curly_parsley_3.delete(0,'end')
		self.fp_curly_parsley_4.delete(0,'end')
		self.fp_flat_coriander_1.delete(0,'end')
		self.fp_flat_coriander_2.delete(0,'end')
		self.fp_flat_coriander_3.delete(0,'end')
		self.fp_flat_coriander_4.delete(0,'end')
		self.fp_green_mint_1.delete(0,'end')
		self.fp_green_mint_2.delete(0,'end')
		self.fp_green_mint_3.delete(0,'end')
		self.fp_green_mint_4.delete(0,'end')
		self.fp_thyme_1.delete(0,'end')
		self.fp_thyme_2.delete(0,'end')
		self.fp_thyme_3.delete(0,'end')
		self.fp_thyme_4.delete(0,'end')
		self.fp_rosemary_1.delete(0,'end')
		self.fp_rosemary_2.delete(0,'end')
		self.fp_rosemary_3.delete(0,'end')
		self.fp_rosemary_4.delete(0,'end')

		self.pots_italian_basil_1.delete(0,'end')
		self.pots_italian_basil_2.delete(0,'end')
		self.pots_italian_basil_3.delete(0,'end')
		self.pots_italian_basil_4.delete(0,'end')
		self.pots_italian_basil_5.delete(0,'end')
		self.pots_italian_basil_6.delete(0,'end')
		self.pots_italian_basil_7.delete(0,'end')
		self.pots_italian_basil_8.delete(0,'end')
		self.pots_italian_basil_9.delete(0,'end')
		self.pots_italian_basil_10.delete(0,'end')
		self.pots_italian_basil_11.delete(0,'end')
		self.pots_italian_basil_12.delete(0,'end')
		self.pots_italian_basil_13.delete(0,'end')
		self.pots_italian_basil_14.delete(0,'end')
		self.pots_italian_basil_15.delete(0,'end')
		self.pots_italian_basil_16.delete(0,'end')
		self.pots_italian_basil_17.delete(0,'end')
		self.pots_flat_coriander_1.delete(0,'end')
		self.pots_flat_coriander_2.delete(0,'end')
		self.pots_flat_coriander_3.delete(0,'end')
		self.pots_flat_coriander_4.delete(0,'end')
		self.pots_flat_coriander_5.delete(0,'end')
		self.pots_flat_coriander_6.delete(0,'end')
		self.pots_flat_coriander_7.delete(0,'end')
		self.pots_flat_coriander_8.delete(0,'end')
		self.pots_flat_coriander_9.delete(0,'end')
		self.pots_flat_coriander_10.delete(0,'end')
		self.pots_flat_coriander_11.delete(0,'end')
		self.pots_flat_coriander_12.delete(0,'end')
		self.pots_flat_coriander_13.delete(0,'end')
		self.pots_flat_coriander_14.delete(0,'end')
		self.pots_flat_coriander_15.delete(0,'end')
		self.pots_flat_coriander_16.delete(0,'end')
		self.pots_flat_coriander_17.delete(0,'end')
		self.pots_thyme_1.delete(0,'end')
		self.pots_thyme_2.delete(0,'end')
		self.pots_thyme_3.delete(0,'end')
		self.pots_thyme_4.delete(0,'end')
		self.pots_thyme_5.delete(0,'end')
		self.pots_thyme_6.delete(0,'end')
		self.pots_thyme_7.delete(0,'end')
		self.pots_thyme_8.delete(0,'end')
		self.pots_thyme_9.delete(0,'end')
		self.pots_thyme_10.delete(0,'end')
		self.pots_thyme_11.delete(0,'end')
		self.pots_thyme_12.delete(0,'end')
		self.pots_thyme_13.delete(0,'end')
		self.pots_thyme_14.delete(0,'end')
		self.pots_thyme_15.delete(0,'end')
		self.pots_thyme_16.delete(0,'end')
		self.pots_thyme_17.delete(0,'end')
		self.pots_green_mint_1.delete(0,'end')
		self.pots_green_mint_2.delete(0,'end')
		self.pots_green_mint_3.delete(0,'end')
		self.pots_green_mint_4.delete(0,'end')
		self.pots_green_mint_5.delete(0,'end')
		self.pots_green_mint_6.delete(0,'end')
		self.pots_green_mint_7.delete(0,'end')
		self.pots_green_mint_8.delete(0,'end')
		self.pots_green_mint_9.delete(0,'end')
		self.pots_green_mint_10.delete(0,'end')
		self.pots_green_mint_11.delete(0,'end')
		self.pots_green_mint_12.delete(0,'end')
		self.pots_green_mint_13.delete(0,'end')
		self.pots_green_mint_14.delete(0,'end')
		self.pots_green_mint_15.delete(0,'end')
		self.pots_green_mint_16.delete(0,'end')
		self.pots_green_mint_17.delete(0,'end')
		self.pots_rosemary_1.delete(0,'end')
		self.pots_rosemary_2.delete(0,'end')
		self.pots_rosemary_3.delete(0,'end')
		self.pots_rosemary_4.delete(0,'end')
		self.pots_rosemary_5.delete(0,'end')
		self.pots_rosemary_6.delete(0,'end')
		self.pots_rosemary_7.delete(0,'end')
		self.pots_rosemary_8.delete(0,'end')
		self.pots_rosemary_9.delete(0,'end')
		self.pots_rosemary_10.delete(0,'end')
		self.pots_rosemary_11.delete(0,'end')
		self.pots_rosemary_12.delete(0,'end')
		self.pots_rosemary_13.delete(0,'end')
		self.pots_rosemary_14.delete(0,'end')
		self.pots_rosemary_15.delete(0,'end')
		self.pots_rosemary_16.delete(0,'end')
		self.pots_rosemary_17.delete(0,'end')
		self.pots_chervil_1.delete(0,'end')
		self.pots_chervil_2.delete(0,'end')
		self.pots_chervil_3.delete(0,'end')
		self.pots_chervil_4.delete(0,'end')
		self.pots_chervil_5.delete(0,'end')
		self.pots_chervil_6.delete(0,'end')
		self.pots_chervil_7.delete(0,'end')
		self.pots_chervil_8.delete(0,'end')
		self.pots_chervil_9.delete(0,'end')
		self.pots_chervil_10.delete(0,'end')
		self.pots_chervil_11.delete(0,'end')
		self.pots_chervil_12.delete(0,'end')
		self.pots_chervil_13.delete(0,'end')
		self.pots_chervil_14.delete(0,'end')
		self.pots_chervil_15.delete(0,'end')
		self.pots_chervil_16.delete(0,'end')
		self.pots_chervil_17.delete(0,'end')
		self.pots_watercress_1.delete(0,'end')
		self.pots_watercress_2.delete(0,'end')
		self.pots_watercress_3.delete(0,'end')
		self.pots_watercress_4.delete(0,'end')
		self.pots_watercress_5.delete(0,'end')
		self.pots_watercress_6.delete(0,'end')
		self.pots_watercress_7.delete(0,'end')
		self.pots_watercress_8.delete(0,'end')
		self.pots_watercress_9.delete(0,'end')
		self.pots_watercress_10.delete(0,'end')
		self.pots_watercress_11.delete(0,'end')
		self.pots_watercress_12.delete(0,'end')
		self.pots_watercress_13.delete(0,'end')
		self.pots_watercress_14.delete(0,'end')
		self.pots_watercress_15.delete(0,'end')
		self.pots_watercress_16.delete(0,'end')
		self.pots_watercress_17.delete(0,'end')
		self.pots_melissa_1.delete(0,'end')
		self.pots_melissa_2.delete(0,'end')
		self.pots_melissa_3.delete(0,'end')
		self.pots_melissa_4.delete(0,'end')
		self.pots_melissa_5.delete(0,'end')
		self.pots_melissa_6.delete(0,'end')
		self.pots_melissa_7.delete(0,'end')
		self.pots_melissa_8.delete(0,'end')
		self.pots_melissa_9.delete(0,'end')
		self.pots_melissa_10.delete(0,'end')
		self.pots_melissa_11.delete(0,'end')
		self.pots_melissa_12.delete(0,'end')
		self.pots_melissa_13.delete(0,'end')
		self.pots_melissa_14.delete(0,'end')
		self.pots_melissa_15.delete(0,'end')
		self.pots_melissa_16.delete(0,'end')
		self.pots_melissa_17.delete(0,'end')
		self.pots_oregano_1.delete(0,'end')
		self.pots_oregano_2.delete(0,'end')
		self.pots_oregano_3.delete(0,'end')
		self.pots_oregano_4.delete(0,'end')
		self.pots_oregano_5.delete(0,'end')
		self.pots_oregano_6.delete(0,'end')
		self.pots_oregano_7.delete(0,'end')
		self.pots_oregano_8.delete(0,'end')
		self.pots_oregano_9.delete(0,'end')
		self.pots_oregano_10.delete(0,'end')
		self.pots_oregano_11.delete(0,'end')
		self.pots_oregano_12.delete(0,'end')
		self.pots_oregano_13.delete(0,'end')
		self.pots_oregano_14.delete(0,'end')
		self.pots_oregano_15.delete(0,'end')
		self.pots_oregano_16.delete(0,'end')
		self.pots_oregano_17.delete(0,'end')
		self.pots_flat_parsley_1.delete(0,'end')
		self.pots_flat_parsley_2.delete(0,'end')
		self.pots_flat_parsley_3.delete(0,'end')
		self.pots_flat_parsley_4.delete(0,'end')
		self.pots_flat_parsley_5.delete(0,'end')
		self.pots_flat_parsley_6.delete(0,'end')
		self.pots_flat_parsley_7.delete(0,'end')
		self.pots_flat_parsley_8.delete(0,'end')
		self.pots_flat_parsley_9.delete(0,'end')
		self.pots_flat_parsley_10.delete(0,'end')
		self.pots_flat_parsley_11.delete(0,'end')
		self.pots_flat_parsley_12.delete(0,'end')
		self.pots_flat_parsley_13.delete(0,'end')
		self.pots_flat_parsley_14.delete(0,'end')
		self.pots_flat_parsley_15.delete(0,'end')
		self.pots_flat_parsley_16.delete(0,'end')
		self.pots_flat_parsley_17.delete(0,'end')
		self.pots_pea_shoots_1.delete(0,'end')
		self.pots_pea_shoots_2.delete(0,'end')
		self.pots_pea_shoots_3.delete(0,'end')
		self.pots_pea_shoots_4.delete(0,'end')
		self.pots_pea_shoots_5.delete(0,'end')
		self.pots_pea_shoots_6.delete(0,'end')
		self.pots_pea_shoots_7.delete(0,'end')
		self.pots_pea_shoots_8.delete(0,'end')
		self.pots_pea_shoots_9.delete(0,'end')
		self.pots_pea_shoots_10.delete(0,'end')
		self.pots_pea_shoots_11.delete(0,'end')
		self.pots_pea_shoots_12.delete(0,'end')
		self.pots_pea_shoots_13.delete(0,'end')
		self.pots_pea_shoots_14.delete(0,'end')
		self.pots_pea_shoots_15.delete(0,'end')
		self.pots_pea_shoots_16.delete(0,'end')
		self.pots_pea_shoots_17.delete(0,'end')

		self.message['text'] = "Cleared. Please, insert ref number and quantities"
		self.message['fg'] = 'black'
		self.message['font'] = ('Helvetica', 8, 'bold')

if __name__ == '__main__':
    window = Tk()
    application = BarcodeAssistant(window)
    window.mainloop()