select VF_CONFIG_CUR_RATES_FUNC ('8','91.16','840','USD to Albanian Lek','22/10/2024') from dual;
select VF_CONFIG_CUR_RATES_FUNC ('8','98.69','978','EUR to Albanian Lek','22/10/2024') from dual;
select * from vf_config_cur_rates_t where effective_date in ('22/10/2024');

