from graphqlclient import GraphQLClient
import json

def extract_data():
    client = GraphQLClient('https://gis-api.aiesec.org/graphql?access_token=0339633ea53bfeada686b9601eec9522be673f1d76034bc81e30173b129b2edc')
    query_ogx_APDs = '''{allOpportunityApplication(
    		filters:
    		{
          person_home_lc:1064
          date_approved:{from:"01/07/2021"}

    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      }
    }'''
    query_ogx_REs = '''{allOpportunityApplication(
    		filters:
    		{
          person_home_lc:1064
          date_realized:{from:"01/07/2021"}

    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      }
    } '''
    query_ogx_FIs = '''{allOpportunityApplication(
    		filters:
    		{
          person_home_lc:1064
          experience_end_date:{from:"01/07/2021"}
     statuses:["finished","completed"]
    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      } }'''

    query_icx_APDs = '''{allOpportunityApplication(
    		filters:
    		{
          opportunity_home_lc:1064
          date_approved:{from:"01/07/2021"}

    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      }
    }'''
    query_icx_REs = '''{allOpportunityApplication(
    		filters:
    		{
          opportunity_home_lc:1064
          date_realized:{from:"01/07/2021"}

    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      }
    } '''
    query_icx_FIs = '''{allOpportunityApplication(
    		filters:
    		{
          opportunity_home_lc:1064
          experience_end_date:{from:"01/07/2021"}
     statuses:["finished","completed"]
    		}

        page:1
        per_page:3000
    	)
    	{
        paging
        {
          total_items
        }
    		data
        {
          person
          {
            id
            full_name
            email

            home_lc
            {
              name
            }
            home_mc
            {
              name
            }
          }
          opportunity
          {
            id
            programme
            { short_name_display }
            host_lc
            {
              name
            }
            home_mc
            {
              name
            }


            opportunity_duration_type{
              duration_type
            }

          }
          slot{
            start_date
            end_date
          }
          status
          updated_at
          date_approved
          date_realized
          experience_end_date


         }
      } }'''

    result = client.execute(query_ogx_APDs)
    data = json.loads(result)
    result_OGX_APDs = process_data(data['data']['allOpportunityApplication']['data'], "O")

    result = client.execute(query_ogx_REs)
    data = json.loads(result)
    result_OGX_REs = process_data(data['data']['allOpportunityApplication']['data'], "O")

    result = client.execute(query_ogx_FIs)
    data = json.loads(result)
    result_OGX_FIs = process_data(data['data']['allOpportunityApplication']['data'], "O")

    result = client.execute(query_icx_APDs)
    data = json.loads(result)
    result_ICX_APDs = process_data(data['data']['allOpportunityApplication']['data'], "I")

    result = client.execute(query_icx_REs)
    data = json.loads(result)
    result_ICX_REs = process_data(data['data']['allOpportunityApplication']['data'], "I")

    result = client.execute(query_icx_FIs)
    data = json.loads(result)
    result_ICX_FIs = process_data(data['data']['allOpportunityApplication']['data'], "I")

    return result_OGX_APDs, result_OGX_REs , result_OGX_FIs, result_ICX_APDs, result_ICX_REs, result_ICX_FIs

def process_data(data,type):
    eps = []
    for ep in data:
        oneEP = []
        oneEP.append(str(ep['person']['id'])+"_"+str(ep['opportunity']['id'])) #reference ID
        oneEP.append(ep['person']['full_name'])
        oneEP.append("https://expa.aiesec.org/people/"+str(ep['person']['id']))
        oneEP.append(ep['person']['email'])
        oneEP.append(type+ep['opportunity']['programme']['short_name_display'])
        oneEP.append(ep['person']['home_lc']['name'].replace(",", " "))
        oneEP.append(ep['person']['home_mc']['name'].replace(",", " "))
        oneEP.append(ep['opportunity']['host_lc']['name'].replace(",", " "))
        oneEP.append(ep['opportunity']['home_mc']['name'].replace(",", " "))
        oneEP.append("https://expa.aiesec.org/opportunities/" + str(ep['opportunity']['id']) + "/")
        if ep['date_approved'] is None:
            oneEP.append(ep['updated_at'][:10])
        else:
            oneEP.append(ep['date_approved'][:10])
        if ep['slot'] is not None:
            oneEP.append(ep['slot']['start_date'])
            oneEP.append(ep['slot']['end_date'])
        else:
            oneEP.append("")
            oneEP.append("")
        if ep['date_realized'] is None:
            oneEP.append("")
        else:
            oneEP.append(ep['date_realized'][:10])
        if ep['experience_end_date'] is None:
            oneEP.append("")
        else:
            oneEP.append(ep['experience_end_date'][:10])

        eps.append(oneEP)

    return eps





