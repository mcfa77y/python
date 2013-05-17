
package com.bricsnet.core.dal.password;
import javax.persistence.Transient;
import javax.persistence.Id;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Transient;

/**
 * Value object for ResetRequest.
 *
 * @author <a href="mailto:daniel.hew@bricsnet.com">Daniel Hew</a>
 * @version @version@
 */

@Entity
@Table(name="ResetRequest")
public class ResetRequestDTO	
   extends java.lang.Object
   implements java.io.Serializable 
{

   private java.lang.Integer id;
   private boolean idHasBeenSet = false;
   private java.lang.String username;
   private boolean usernameHasBeenSet = false;
   private java.lang.String uid;
   private boolean uidHasBeenSet = false;
   private java.sql.Timestamp expDate;
   private boolean expDateHasBeenSet = false;

   

   public ResetRequestDTO()
   {
   }

   public ResetRequestDTO( java.lang.Integer id,java.lang.String username,java.lang.String uid,java.sql.Timestamp expDate )
   {
	  this.id = id;
	  idHasBeenSet = true;
	  this.username = username;
	  usernameHasBeenSet = true;
	  this.uid = uid;
	  uidHasBeenSet = true;
	  this.expDate = expDate;
	  expDateHasBeenSet = true;
	  
   }

   //TODO Cloneable is better than this !
   public ResetRequestDTO( ResetRequestDTO otherValue )
   {
	  this.id = otherValue.id;
	  idHasBeenSet = true;
	  this.username = otherValue.username;
	  usernameHasBeenSet = true;
	  this.uid = otherValue.uid;
	  uidHasBeenSet = true;
	  this.expDate = otherValue.expDate;
	  expDateHasBeenSet = true;

	  
   }

   @Transient


   @Transient
@Id
@Transient
public java.lang.Integer getId()
   {
	  return this.id;
   }

   public void setId( java.lang.Integer id )
   {
	this.id = id;
	  idHasBeenSet = true;

	
   }

   @Transient
@Transient
public boolean idHasBeenSet(){
	  return idHasBeenSet;
   }
   @Transient
@Transient
public java.lang.String getUsername()
   {
	  return this.username;
   }

   public void setUsername( java.lang.String username )
   {
	this.username = username;
	  usernameHasBeenSet = true;

   }

   @Transient
@Transient
public boolean usernameHasBeenSet(){
	  return usernameHasBeenSet;
   }
   @Transient
@Transient
public java.lang.String getUid()
   {
	  return this.uid;
   }

   public void setUid( java.lang.String uid )
   {
	this.uid = uid;
	  uidHasBeenSet = true;

   }

   @Transient
@Transient
public boolean uidHasBeenSet(){
	  return uidHasBeenSet;
   }
   @Transient
@Transient
public java.sql.Timestamp getExpDate()
   {
	  return this.expDate;
   }

   public void setExpDate( java.sql.Timestamp expDate )
   {
	this.expDate = expDate;
	  expDateHasBeenSet = true;

   }

   @Transient
@Transient
public boolean expDateHasBeenSet(){
	  return expDateHasBeenSet;
   }

   public String toString()
   {
	  StringBuffer str = new StringBuffer("{");

	  str.append("id=" + getId() + " " + "username=" + getUsername() + " " + "uid=" + getUid() + " " + "expDate=" + getExpDate());
	  str.append('}');

	  return(str.toString());
   }

   /**
    * A Value Object has an identity if the attributes making its Primary Key have all been set. An object without identity is never equal to any other object.
    *
    * @return true if this instance has an identity.
    */
   protected boolean hasIdentity()
   {
	  return idHasBeenSet;
   }

   public boolean equals(Object other)
   {
      if (this == other)
         return true;
	  if ( ! hasIdentity() ) return false;
	  if (other instanceof ResetRequestDTO)
	  {
		 ResetRequestDTO that = (ResetRequestDTO) other;
		 if ( ! that.hasIdentity() ) return false;
		 boolean lEquals = true;
		 if( this.id == null )
		 {
			lEquals = lEquals && ( that.id == null );
		 }
		 else
		 {
			lEquals = lEquals && this.id.equals( that.id );
		 }

		 lEquals = lEquals && isIdentical(that);

		 return lEquals;
	  }

	 return false;
   }

   public boolean isIdentical(Object other)
   {
	  if (other instanceof ResetRequestDTO)
	  {
		 ResetRequestDTO that = (ResetRequestDTO) other;
		 boolean lEquals = true;
		 if( this.username == null )
		 {
			lEquals = lEquals && ( that.username == null );
		 }
		 else
		 {
			lEquals = lEquals && this.username.equals( that.username );
		 }
		 if( this.uid == null )
		 {
			lEquals = lEquals && ( that.uid == null );
		 }
		 else
		 {
			lEquals = lEquals && this.uid.equals( that.uid );
		 }
		 if( this.expDate == null )
		 {
			lEquals = lEquals && ( that.expDate == null );
		 }
		 else
		 {
			lEquals = lEquals && this.expDate.equals( that.expDate );
		 }

		 return lEquals;
	  }

	 return false;
   }

   //TODO:DTO is not Auditable, remove everything below the hashCode declaration.
 public int hashCode(){
	  int result = 17;
      result = 37*result + ((this.id != null) ? this.id.hashCode() : 0);

      result = 37*result + ((this.username != null) ? this.username.hashCode() : 0);

      result = 37*result + ((this.uid != null) ? this.uid.hashCode() : 0);

      result = 37*result + ((this.expDate != null) ? this.expDate.hashCode() : 0);

	  return result;
   }

	protected static boolean merged = false;
	protected static java.util.Map<String, String> formatMap =
		new java.util.HashMap<String, String>();
	protected static java.util.Map<String, Integer> maxLengths =
		new java.util.HashMap<String, Integer>();
	protected static java.util.Map<String, Number> maxValues =
		new java.util.HashMap<String, Number>();
	protected static java.util.Map<String, Number> minValues =
		new java.util.HashMap<String, Number>();
	//TODO:Remove History Properties.
protected static java.util.Set<String> historyProperties =
		new java.util.HashSet<String>();
	static {

	// handle bricsnet.localize
		formatMap.put("id", "#"); // java.lang.Integer
	// handle bricsnet.validate
	// bricsnet.hiddenFromHistory
		historyProperties.add("id");

	// handle bricsnet.localize
	// handle bricsnet.validate
	// bricsnet.hiddenFromHistory
		historyProperties.add("username");

	// handle bricsnet.localize
	// handle bricsnet.validate
	// bricsnet.hiddenFromHistory
		historyProperties.add("uid");

	// handle bricsnet.localize
	// handle bricsnet.validate
	// bricsnet.hiddenFromHistory
		historyProperties.add("expDate");

	}

	@Transient
@Transient
public java.util.Map<String, String> getFormatMap() {
		merge();
		return formatMap;
	}
	@Transient
@Transient
public java.util.Map<String, Integer> getMaxLengthsMap() {
		merge();
		return maxLengths;
	}
	@Transient
@Transient
public java.util.Map<String, Number> getMaxValuesMap() {
		merge();
		return maxValues;
	}
	@Transient
@Transient
public java.util.Map<String, Number> getMinValuesMap() {
		merge();
		return minValues;
	}
	// only Auditable objects really need to implement this, 
	// but it's simpler to just give it to everybody
	@Transient
@Transient
public java.util.Set<String> getHistoryProperties() {
		merge();
		return historyProperties;
	}
	private synchronized void merge() {
		if(merged) return;
		merged = true;
	}

}
